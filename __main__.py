# -*- coding: utf-8 -*-

import random
import vk_api
from vk_api.keyboard import VkKeyboard, VkKeyboardColor
from vk_api.longpoll import VkLongPoll, VkEventType
import functions_for_main
import sys


def main():

    token = '4673adc76e914707c6abf301549063dc5f6d7fe6016d00b698bbba46a2ae3f777f2521bb20ffdbe4c430a'
    token_app = '8be8e9448be8e9448be8e944088b9aa11988be88be8e944d539e56536f403dbc3f67b7d'

    vk_session = vk_api.VkApi(token=token)  # Токен бота

    vk = vk_session.get_api()

    keyboard = VkKeyboard(one_time=False)

    def write_msg(user_id, message):
        vk_session.method(
            'messages.send',
            {
                'user_id': user_id,
                'message': message,
                'random_id': random.randint(0, 2048)
            }
        )

    test_group = -120254617
    test_album = 230633050
    print(functions_for_main.get_a_funny_shit(token_app))
    longpoll = VkLongPoll(vk_session)

    # "Прослушка" входящих сообщения и ответы на них

    for event in longpoll.listen():

        if event.type == VkEventType.MESSAGE_NEW:
            if event.to_me:

                # Получение имени пользователя
                user_get = vk.users.get(user_ids=event.user_id)
                user_get = user_get[0]
                first_name = user_get['first_name']

                request = event.text.lower()
                if request == "привет" or request == "хай" or request == "здарова":
                    write_msg(event.user_id, "Привет, " + first_name)
                    if first_name == "Сергей":
                        write_msg(event.user_id, "Слушай Серый, не хочешь пРиКоЛьНуТьСя?)))")

                elif request == "хочу":
                    functions_for_main.funny_keyboard(vk_session,event.user_id, "))0)")

                elif request == "прикольнуться":
                    vk_session.method(
                        'messages.send',
                        {
                            'user_id': event.user_id,
                            'random_id': random.randint(0, 2048),
                            "attachment": functions_for_main.get_a_funny_shit(token_app)

                        }
                    )

                elif request == "сам пошел":
                    write_msg(event.user_id, "Нихуя себе, сам пошел")

                elif request.isdigit():
                    write_msg(event.user_id, "⠏⠕⠱⠑⠇ ⠝⠁⠓⠥⠯")

                elif request == "старт" or request == "начать":
                    functions_for_main.send_keyboard(vk_session, event.user_id, "Опять работа")

                elif request == "не всегда смешная картинка":
                    vk_session.method(
                        'messages.send',
                    {
                        'user_id': event.user_id,
                        'message': functions_for_main.laugh(),
                        'random_id': random.randint(0, 2048),
                        "attachment": functions_for_main.get_photos(token_app)

                    }
                )

                elif request == "стоп":
                    vk_session.method(
                        'messages.send',
                        {
                            'user_id': event.user_id,
                            'message': "Ладно",
                            'random_id': random.randint(0, 2048),
                            'keyboard': keyboard.get_empty_keyboard()
                        }
                    )
                elif request == "что умеешь?" or request == "что умеешь":
                    write_msg(event.user_id, "Могу только картинки отправлять")
                else:
                    write_msg(event.user_id, "Не понимаю")


if __name__ == '__main__':
    main()

# Доделать
