import json

from botbuilder.core import MessageFactory, UserState
from botbuilder.dialogs import (
    ComponentDialog,
    WaterfallDialog,
    WaterfallStepContext,
    DialogTurnResult,
    PromptOptions,
    TextPrompt
)
from botbuilder.schema import ActivityTypes, Activity

from ms_bot.helpers.telegram_helper import rm_tg_message
from ms_bot.lib.messages import confirm_kb, SEND_GRAFIK_KB
from setup.logger import CustomLogger

logger = CustomLogger.get_logger('bot')


class GrafikDialog(ComponentDialog):
    def __init__(
            self,
            user_state: UserState,
            dialog_id: str = None
    ):
        super(GrafikDialog, self).__init__(dialog_id or GrafikDialog.__name__)

        self.user_state = user_state
        self.user_profile_accessor = self.user_state.create_property("CustomerProfile")

        self.add_dialog(TextPrompt(TextPrompt.__name__))
        self.add_dialog(
            WaterfallDialog(
                "GrafikDialog",
                [
                    self.confirmation_step,
                    self.local_menu_step,
                    self.last_step,

                ]
            )
        )

        self.initial_dialog_id = "GrafikDialog"

    async def confirmation_step(self, step_context: WaterfallStepContext) -> DialogTurnResult:
        logger.debug('confirmation_step %s', GrafikDialog.__name__)

        return await step_context.prompt(
            TextPrompt.__name__, PromptOptions(
                prompt=Activity(
                    channel_data=json.dumps(confirm_kb('графика работы')),
                    type=ActivityTypes.message,
                ),
                retry_prompt=MessageFactory.text('Зробіть вибір, натиснувши на відповідну кнопку вище'),
            )
        )

    async def local_menu_step(self, step_context: WaterfallStepContext) -> DialogTurnResult:
        logger.debug('local_menu_step %s', GrafikDialog.__name__)

        found_choice = step_context.result

        if found_choice == 'KEY_CALLBACK:yes':

            return await step_context.prompt(
                TextPrompt.__name__, PromptOptions(
                    prompt=Activity(
                        channel_data=json.dumps(SEND_GRAFIK_KB),
                        type=ActivityTypes.message,
                    ),
                    retry_prompt=MessageFactory.text('Зробіть вибір, натиснувши на відповідну кнопку вище'),
                )
            )
        elif found_choice == 'KEY_CALLBACK:no':
            await step_context.context.send_activity('Задайте вопрос оператору')
            return await step_context.cancel_all_dialogs()

        else:
            return await step_context.cancel_all_dialogs(True)

    async def last_step(self, step_context: WaterfallStepContext) -> DialogTurnResult:
        logger.debug('last_step %s', GrafikDialog.__name__)
        found_choice = step_context.result

        if found_choice == 'KEY_CALLBACK:otpusk5':
            await step_context.context.send_activity('Задать вопрос оператору')
            return await step_context.cancel_all_dialogs(True)

        else:
            await step_context.context.send_activity('Тут будет соответствующий раздел и информация')
            return await step_context.cancel_all_dialogs(True)