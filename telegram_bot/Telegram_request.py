import requests
from .models import TelegramSettings


def RequestTelegram(tg_name, tg_phone, tg_email, tg_comment):
    if TelegramSettings.objects.get(pk=1):
        setting = TelegramSettings.objects.get(pk=1)
        token = str(setting.tg_token)
        chat_id = str(setting.tg_chat)
        text = str(setting.tg_message)
        api = 'https://api.telegram.org/bot'
        method = api + token + '/sendMessage'
        if text.find('{') and text.find('}') and text.rfind('{') and text.rfind('}'):
            part_1 = text[:text.find('{')]
            part_2 = text[text.find('}') + 1:text.find('{{')]
            part_3 = text[text.find('}}') + 2:text.find('{{{')]
            part_4 = text[text.find('}}}') + 3:text.rfind('{')]
            part_5 = text[text.rfind('}'):-1]
            print(text)
            text_slice = part_1 + tg_name + part_2 + tg_phone + part_3 + tg_email + part_4 + tg_comment + part_5
        else:
            text_slice = text
        try:
            print('text_slice', text_slice)
            req = requests.post(method, data={
                'chat_id': chat_id,
                'text': text_slice
            })
        except:
            pass
        finally:
            if req.status_code != 200:
                print('Ошибка отправки!')
            elif req.status_code == 500:
                print('Ошибка 500')
            else:
                print('Сообщение отправлено')
