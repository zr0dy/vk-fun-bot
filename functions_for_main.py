import random
import vk_api
from vk_api.keyboard import VkKeyboard, VkKeyboardColor
from vk_api.longpoll import VkLongPoll, VkEventType


def laugh():
    list_of_letter = ['х', 'а']
    xax_string = ''
    random_border = random.randint(4, 8)
    for i in range(0, random_border):
        xax_string += list_of_letter[random.randint(0, 1)]
        i += 1
    return xax_string


def get_photos(token):
    list_of_group = [-120254617, -93082454, -109125388]
    id_group = list_of_group[random.randint(0, len(list_of_group) - 1)]
    vk_session_app = vk_api.VkApi(token=token)
    vk = vk_session_app.get_api()
    max_num = vk.photos.get(owner_id=id_group, album_id='wall', count=1)['count']
    num = random.randint(1, max_num)
    get_picture = vk.photos.get(owner_id=id_group, album_id='wall', count=1, offset=num)['items']
    buf = []
    for element in get_picture:
        buf.append('photo' + str(id_group) + '_' + str(element['id']))
    attachment = ','.join(buf)
    return attachment


def send_keyboard(vk_session, key_us_id, mess):
    keyboard = VkKeyboard(one_time=False)

    keyboard.add_button('Смешной анекдот', color=VkKeyboardColor.POSITIVE)
    keyboard.add_line()
    keyboard.add_button('Не всегда смешная картинка', color=VkKeyboardColor.POSITIVE)

    keyboard.add_line()  # Переход на вторую строку
    keyboard.add_openlink_button(label="Если ничего не хочется, можно сюда", link="https://natribu.org/ru/")

    vk_session.method(
        'messages.send',
        {
            'user_id': key_us_id,
            'message': mess,
            'random_id': random.randint(0, 2048),
            'keyboard': keyboard.get_keyboard()
        }
    )


def funny_keyboard(vk_session, key_us_id, mess):

    keyboard = VkKeyboard(one_time=False)
    keyboard.add_button("пРиКоЛьНуТьСя", color=VkKeyboardColor.PRIMARY)

    vk_session.method(
        'messages.send',
        {
            'user_id': key_us_id,
            'message': mess,
            'random_id': random.randint(0, 2048),
            'keyboard': keyboard.get_keyboard()
        }
    )


def get_a_funny_shit(token_app):

    id_group = -159708114

    vk_session = vk_api.VkApi(token=token_app)
    vk = vk_session.get_api()
    max_num = vk.photos.get(owner_id=id_group, album_id='wall', count=1)['count']
    num = random.randint(1, max_num)
    get_picture = vk.photos.get(owner_id=id_group, album_id='wall', count=5, offset=num)['items']
    buf = []
    for element in get_picture:
        buf.append('photo' + str(id_group) + '_' + str(element['id']))
    attachment = ','.join(buf)
    return attachment

