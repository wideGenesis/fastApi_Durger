import aiofiles
import aiohttp

from botbuilder.core import ConversationState, UserState, BotTelemetryClient, NullTelemetryClient
from botbuilder.dialogs import ComponentDialog, WaterfallDialog, WaterfallStepContext, DialogTurnResult
from botbuilder.schema import Attachment

from api.nlp import resolve_category_of_text
from ms_bot.dialogs.bolnichyi_dialog import BolnichnyiDialog
from ms_bot.dialogs.grafik_dialog import GrafikDialog
from ms_bot.dialogs.ocenka_celi_dialog import OcenkaCeliDialog
from ms_bot.dialogs.otpusk_dialog import OtpuskDialog
from ms_bot.dialogs.raschetnyi_list_dialog import RaschetnyiListDialog
from ms_bot.dialogs.spravka_dialog import SpravkaDialog
from ms_bot.dialogs.spravka_dohod_dialog import SpravkaDohodDialog
from ms_bot.helpers.speech_recognition import recognize_from_filename
from setup.logger import CustomLogger

logger = CustomLogger.get_logger('bot')


class MainDialog(ComponentDialog):
    def __init__(
            self,
            conversation_state: ConversationState,
            user_state: UserState,
            telemetry_client: BotTelemetryClient = None,

    ):
        super(MainDialog, self).__init__(MainDialog.__name__)
        self.telemetry_client = telemetry_client or NullTelemetryClient()

        # Add state property accessors
        self.user_profile_accessor = user_state.create_property("CustomerProfile")

        self.add_dialog(OtpuskDialog(user_state, OtpuskDialog.__name__))
        self.add_dialog(RaschetnyiListDialog(user_state, RaschetnyiListDialog.__name__))
        self.add_dialog(BolnichnyiDialog(user_state, BolnichnyiDialog.__name__))
        self.add_dialog(OcenkaCeliDialog(user_state, OcenkaCeliDialog.__name__))
        self.add_dialog(SpravkaDohodDialog(user_state, SpravkaDohodDialog.__name__))
        self.add_dialog(GrafikDialog(user_state, GrafikDialog.__name__))
        self.add_dialog(SpravkaDialog(user_state, SpravkaDialog.__name__))

        self.add_dialog(
            WaterfallDialog(
                "MainDialog",
                [
                    self.detect_channel_step,
                    self.parse_audio_step,
                    self.speech_to_text_step,
                    self.send_text_to_nlp_step,
                    self.routing_step,
                ]
            )
        )
        MainDialog.telemetry_client = self.telemetry_client

        self.initial_dialog_id = "MainDialog"
        self.conversation_state = conversation_state
        self.user_state = user_state
        self.member_id = None

    async def detect_channel_step(self, step_context: WaterfallStepContext) -> DialogTurnResult:
        logger.debug('detect_channel_step %s', MainDialog.__name__)
        if step_context.context.activity.channel_id != 'telegram':
            await step_context.context.send_activity('Channel not supported')
            return await step_context.end_dialog()

        self.member_id = step_context.context.activity.from_property.id
        await step_context.context.send_activity('Приветствую Вас! DEMO-HR-NLP-BOT на связи 🦾')
        return await step_context.next([])

    async def parse_audio_step(self, step_context: WaterfallStepContext) -> DialogTurnResult:
        logger.debug('parse_audio_step %s', MainDialog.__name__)
        activity = step_context.context.activity
        try:
            attachment: Attachment = activity.attachments[0]
        except Exception:
            return await step_context.next(False)

        await _get_save_file(attachment.content_url, self.member_id)

        return await step_context.next([])

    async def speech_to_text_step(self, step_context: WaterfallStepContext) -> DialogTurnResult:
        logger.debug('speech_to_text_step %s', MainDialog.__name__)
        if step_context.result is False:
            print(step_context.context.activity.text)
            return await step_context.next(str(step_context.context.activity.text))

        recon_result = await recognize_from_filename(self.member_id)
        await step_context.context.send_activity(f'Вы сказали 🔉: {str(recon_result)}')
        return await step_context.next(str(recon_result))

    async def send_text_to_nlp_step(self, step_context: WaterfallStepContext) -> DialogTurnResult:
        logger.debug('send_text_to_nlp_step %s', MainDialog.__name__)
        answer = await resolve_category_of_text(str(step_context.result), '4')
        return await step_context.next(answer)

    async def routing_step(self, step_context: WaterfallStepContext) -> DialogTurnResult:
        logger.debug('routing_step %s', MainDialog.__name__)

        if str(step_context.result) == 'otpusk':
            return await step_context.begin_dialog(OtpuskDialog.__name__)

        elif str(step_context.result) == 'raschetnyi_list':
            return await step_context.begin_dialog(RaschetnyiListDialog.__name__)

        elif str(step_context.result) == 'bolnichnyi':
            return await step_context.begin_dialog(BolnichnyiDialog.__name__)

        elif str(step_context.result) == 'ocenka_i_celi':
            return await step_context.begin_dialog(OcenkaCeliDialog.__name__)

        elif str(step_context.result) == 'login_parol':
            return await step_context.begin_dialog(OcenkaCeliDialog.__name__)

        elif str(step_context.result) == 'spravka_dohod':
            return await step_context.begin_dialog(SpravkaDohodDialog.__name__)

        elif str(step_context.result) == 'grafik':
            return await step_context.begin_dialog(GrafikDialog.__name__)

        elif str(step_context.result) == 'spravka':
            return await step_context.begin_dialog(SpravkaDialog.__name__)

        else:
            await step_context.context.send_activity('Задайте вопрос оператору')
            return await step_context.cancel_all_dialogs()


async def _get_save_file(file_url: str, member_id: int):
    async with aiohttp.ClientSession() as session:
        async with session.get(file_url) as resp:
            assert resp.status == 200
            data = await resp.read()

    async with aiofiles.open(f'media/{member_id}_audio.ogg', "wb") as outfile:
        await outfile.write(data)

    return

#
# async def _get_nlp_response(_message: str, _model: str):
#     endpoint = 'https://hr-demo.azurewebsites.net/test'
#     headers = {
#         'Content-Type': 'application/json',
#     }
#     payload = {
#         'message': _message,
#         'model': _model,
#     }
#
#     try:
#         response = requests.get(
#             endpoint,
#             params=payload,
#             headers=headers
#         )
#     except Exception as e:
#         print('_get_nlp_response: ', e)
#         return
#
#     if response.status_code not in [200, 201, 202]:
#         raise ValueError('Response error: %s' % response.text)
#     res = response.text.split(' / ')
#
#     return res[0]