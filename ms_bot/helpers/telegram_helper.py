import json

from botbuilder.core import TurnContext
from botbuilder.schema import Activity, ActivityTypes
from setup.logger import CustomLogger
from config.conf import PROJECT_CONF


logger = CustomLogger.get_logger('bot')


async def rm_tg_message(turn_context: TurnContext, chat_id, message_id):
    delete_message = {
        'method': 'deleteMessage',
        'parameters': {
            'chat_id': int(chat_id),
            'message_id': int(message_id)
        }
    }

    await turn_context.send_activities(
        [
            Activity(
                channel_data=json.dumps(delete_message),
                type=ActivityTypes.message,
            )
        ]
    )
    return
