from botbuilder.core import ConversationState, UserState, BotTelemetryClient, NullTelemetryClient
from botbuilder.dialogs import ComponentDialog, WaterfallDialog, WaterfallStepContext, DialogTurnResult

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
        self.add_dialog(
            WaterfallDialog(
                "MainDialog",
                [
                    self.detect_channel_step,
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
        return await step_context.end_dialog()
