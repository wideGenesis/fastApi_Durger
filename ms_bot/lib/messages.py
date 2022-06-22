
BOT_MESSAGES = {
    'welcome_without_lang': 'Вітаю!',
    'next': 'далі',
    'main_menu': 'Головне меню',
    'buy': '👋🏼 До побачення! Якщо потрібно продовжити, наберіть будь-яке повідомлення',
    'error': 'Невідома помилка! \n  \nВведіть будь-яке повідомлення: ',
    'exceptions_occurs': 'Зовнішній сервіс повідомив про помилку❗️  \n  \n'
                         'Зачекайте кілька хвилин і надрукуйте повідомлення, '
                         'щоб перезапустити діалог🔄  \n  \nЯкщо помилка повторюватиметься, зв\'яжіться з розробниками '
                         '(telegram @ )',
    'confirm_question': 'Ваш вопрос касается {}?'
}

# CONFIRM_KB = {
#     'method': 'sendMessage',
#     'parameters': {
#         'text': f"{BOT_MESSAGES['confirm_question'].format()}",
#         'reply_markup': {
#             'inline_keyboard': [
#                 [
#                     {
#                         'text': '🟢 Да',
#                         'callback_data': 'KEY_CALLBACK:yes'
#                     }
#                 ],
#                 [
#                     {
#                         'text': '🔴 Нет',
#                         'callback_data': 'KEY_CALLBACK:no'
#                     }
#                 ],
#             ]
#         }
#     }
# }


def confirm_kb(text: str) -> dict:
    return {
        'method': 'sendMessage',
        'parameters': {
        'text': f"{BOT_MESSAGES['confirm_question'].format(text)}",
        'reply_markup': {
            'inline_keyboard': [
                [
                    {
                        'text': '🟢 Да',
                        'callback_data': 'KEY_CALLBACK:yes'
                    }
                ],
                [
                    {
                        'text': '🔴 Нет',
                        'callback_data': 'KEY_CALLBACK:no'
                    }
                ],
            ]
        }
    }
}


SEND_OTPUSK_KB = {
    'method': 'sendMessage',
    'parameters': {
        'text': 'Зробіть вибір:',
        'reply_markup': {
            'inline_keyboard': [
                [
                    {
                        'text': 'Посмотреть график отпусков',
                        'callback_data': 'KEY_CALLBACK:otpusk1'
                    }
                ],
                [
                    {
                        'text': 'Количество дней отпуска',
                        'callback_data': 'KEY_CALLBACK:otpusk2'
                    }
                ],
                [
                    {
                        'text': 'Сколько я могу взять дней отпуска',
                        'callback_data': 'KEY_CALLBACK:otpusk3'
                    }
                ],
[
                    {
                        'text': 'Когда мне выходить на работу, дата выхода',
                        'callback_data': 'KEY_CALLBACK:otpusk4'
                    }
                ],
[
                    {
                        'text': 'Задать вопрос оператору',
                        'callback_data': 'KEY_CALLBACK:otpusk5'
                    }
                ],
            ]
        }
    }
}

SEND_BOLNICHNYI_KB = {
    'method': 'sendMessage',
    'parameters': {
        'text': 'Зробіть вибір:',
        'reply_markup': {
            'inline_keyboard': [
                [
                    {
                        'text': 'Подать заявку про отсутствие больничного',
                        'callback_data': 'KEY_CALLBACK:bolnichnyi1'
                    }
                ],
                [
                    {
                        'text': 'Когда будет выплата по больничному?',
                        'callback_data': 'KEY_CALLBACK:bolnichnyi2'
                    }
                ],
                [
                    {
                        'text': 'Задать вопрос оператору',
                        'callback_data': 'KEY_CALLBACK:bolnichnyi3'
                    }
                ],
            ]
        }
    }
}

SEND_GRAFIK_KB = {
    'method': 'sendMessage',
    'parameters': {
        'text': 'Зробіть вибір:',
        'reply_markup': {
            'inline_keyboard': [
                [
                    {
                        'text': 'Узнать график работы',
                        'callback_data': 'KEY_CALLBACK:grafik1'
                    }
                ],
                [
                    {
                        'text': 'Не верно указан график работы',
                        'callback_data': 'KEY_CALLBACK:grafik2'
                    }
                ],
                [
                    {
                        'text': 'Задать вопрос оператору',
                        'callback_data': 'KEY_CALLBACK:grafik3'
                    }
                ],
            ]
        }
    }
}

SEND_OCENKA_KB = {
    'method': 'sendMessage',
    'parameters': {
        'text': 'Зробіть вибір:',
        'reply_markup': {
            'inline_keyboard': [
                [
                    {
                        'text': 'Получить ифнормацию по ежегодной оценке',
                        'callback_data': 'KEY_CALLBACK:ocenka1'
                    }
                ],
                [
                    {
                        'text': 'Не могу просмотреть ежегодную оценку',
                        'callback_data': 'KEY_CALLBACK:ocenka2'
                    }
                ],
                [
                    {
                        'text': 'Узнать свой грейд',
                        'callback_data': 'KEY_CALLBACK:ocenka3'
                    }
                ],
                [
                    {
                        'text': 'Задать вопрос оператору',
                        'callback_data': 'KEY_CALLBACK:ocenka4'
                    }
                ],
            ]
        }
    }
}

SEND_RASCHETNYI_KB = {
    'method': 'sendMessage',
    'parameters': {
        'text': 'Зробіть вибір:',
        'reply_markup': {
            'inline_keyboard': [
                [
                    {
                        'text': 'Получить расчетный лист',
                        'callback_data': 'KEY_CALLBACK:list1'
                    }
                ],
                [
                    {
                        'text': 'Узнать срок выдачи расчетного листа',
                        'callback_data': 'KEY_CALLBACK:list2'
                    }
                ],
                [
                    {
                        'text': 'Я не могу скачать свой расчетный лист',
                        'callback_data': 'KEY_CALLBACK:list3'
                    }
                ],
                [
                    {
                        'text': 'Задать вопрос оператору',
                        'callback_data': 'KEY_CALLBACK:list4'
                    }
                ],
            ]
        }
    }
}

SEND_SPRAVKA_KB = {
    'method': 'sendMessage',
    'parameters': {
        'text': 'Зробіть вибір:',
        'reply_markup': {
            'inline_keyboard': [
                [
                    {
                        'text': 'Справка с места работы',
                        'callback_data': 'KEY_CALLBACK:spravka1'
                    }
                ],
                [
                    {
                        'text': 'Подтверждение периода',
                        'callback_data': 'KEY_CALLBACK:spravka2'
                    }
                ],
                [
                    {
                        'text': 'Копия трудовой',
                        'callback_data': 'KEY_CALLBACK:spravka3'
                    }
                ],
                [
                    {
                        'text': 'Срок выдачи справки',
                        'callback_data': 'KEY_CALLBACK:spravka4'
                    }
                ],
                [
                    {
                        'text': 'Не могу заказать справку с места работы',
                        'callback_data': 'KEY_CALLBACK:spravka5'
                    }
                ],
                [
                    {
                        'text': 'Задать вопрос оператору',
                        'callback_data': 'KEY_CALLBACK:spravka6'
                    }
                ],
            ]
        }
    }
}

SEND_DOHOD_KB = {
    'method': 'sendMessage',
    'parameters': {
        'text': 'Зробіть вибір:',
        'reply_markup': {
            'inline_keyboard': [
                [
                    {
                        'text': 'О заработной плате',
                        'callback_data': 'KEY_CALLBACK:dohod1'
                    }
                ],
                [
                    {
                        'text': 'Справка (алименты, штрафы)',
                        'callback_data': 'KEY_CALLBACK:dohod2'
                    }
                ],
                [
                    {
                        'text': 'МСЕК, субсидии',
                        'callback_data': 'KEY_CALLBACK:dohod3'
                    }
                ],
                [
                    {
                        'text': 'Срок готовности справки',
                        'callback_data': 'KEY_CALLBACK:dohod4'
                    }
                ],
                [
                    {
                        'text': 'График выплаты зароботной платы',
                        'callback_data': 'KEY_CALLBACK:dohod5'
                    }
                ],
                [
                    {
                        'text': 'Не могу получить справку о доходах',
                        'callback_data': 'KEY_CALLBACK:dohod6'
                    }
                ],
                [
                    {
                        'text': 'Задать вопрос оператору',
                        'callback_data': 'KEY_CALLBACK:dohod7'
                    }
                ],
            ]
        }
    }
}