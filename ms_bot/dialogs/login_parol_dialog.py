from botbuilder.core import MessageFactory, CardFactory, UserState
from botbuilder.dialogs import (
    ComponentDialog,
    WaterfallDialog,
    WaterfallStepContext,
    DialogTurnResult,
    PromptOptions,
    TextPrompt, ChoicePrompt
)
from botbuilder.schema import HeroCard, CardAction, ActionTypes, InputHints

from setup.logger import CustomLogger

logger = CustomLogger.get_logger('bot')


class LoginParolDialog(ComponentDialog):
    def __init__(
            self,
            user_state: UserState,
            dialog_id: str = None
    ):
        super(LoginParolDialog, self).__init__(dialog_id or LoginParolDialog.__name__)

        self.user_state = user_state
        self.user_profile_accessor = self.user_state.create_property("CustomerProfile")

        self.add_dialog(ChoicePrompt(ChoicePrompt.__name__))
        self.add_dialog(TextPrompt(TextPrompt.__name__))
        self.add_dialog(
            WaterfallDialog(
                "LoginParolDialog",
                [
                    self.confirmation_step,
                    self.local_menu_step,
                    self.last_step,

                ]
            )
        )

        self.initial_dialog_id = "LoginParolDialog"

    async def confirmation_step(self, step_context: WaterfallStepContext) -> DialogTurnResult:
        logger.debug('confirmation_step %s', LoginParolDialog.__name__)
        prompt_text = MessageFactory.list([])
        prompt_text.attachments.append(self.create_hero_card_question())
        await step_context.context.send_activity(prompt_text)
        prompt_message = MessageFactory.text('⏳', InputHints.expecting_input)
        return await step_context.prompt(TextPrompt.__name__, PromptOptions(prompt=prompt_message))

    async def local_menu_step(self, step_context: WaterfallStepContext) -> DialogTurnResult:
        logger.debug('local_menu_step %s', LoginParolDialog.__name__)

        found_choice = step_context.result

        if found_choice == 'yes':
            prompt_text = MessageFactory.list([])
            prompt_text.attachments.append(self.create_hero_card_local_menu())
            await step_context.context.send_activity(prompt_text)
            prompt_message = MessageFactory.text('⏳', InputHints.expecting_input)
            return await step_context.prompt(TextPrompt.__name__, PromptOptions(prompt=prompt_message))

        elif found_choice == 'no':
            await step_context.context.send_activity('Задайте вопрос оператору')
            return await step_context.cancel_all_dialogs()

        else:
            return await step_context.cancel_all_dialogs(True)

    async def last_step(self, step_context: WaterfallStepContext) -> DialogTurnResult:
        logger.debug('last_step %s', LoginParolDialog.__name__)

        await step_context.context.send_activity('Тут будет соответствующий раздел и информация')
        return await step_context.cancel_all_dialogs(True)

    def create_hero_card_question(self):
        card = HeroCard(
            text='Ваш вопрос касается отпуска?',
            buttons=[
                CardAction(
                    type=ActionTypes.im_back,
                    title='Да',
                    value='yes',
                ),
                CardAction(
                    type=ActionTypes.im_back,
                    title='Нет',
                    value='no',
                )
            ],
        )
        return CardFactory.hero_card(card)

    def create_hero_card_local_menu(self):
        card = HeroCard(
            text='🤠',
            buttons=[
                CardAction(
                    type=ActionTypes.im_back,
                    title='Посмотреть график отпусков',
                    value='1',
                ),
                CardAction(
                    type=ActionTypes.im_back,
                    title='Количество дней отпуска',
                    value='2',
                ),
                CardAction(
                    type=ActionTypes.im_back,
                    title='Сколько я могу взять дней отпуска',
                    value='3',
                ),
                CardAction(
                    type=ActionTypes.im_back,
                    title='Когда мне выходить на работу, дата выхода',
                    value='4',
                ),
                CardAction(
                    type=ActionTypes.im_back,
                    title='Задать вопрос оператору',
                    value='5',
                ),
            ],
        )
        return CardFactory.hero_card(card)
