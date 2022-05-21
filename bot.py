import random
import time

import constants
import Token

import telebot
from telebot import types


bot = telebot.TeleBot(Token.token)


# logger = telebot.logger
# telebot.logger.setLevel(logging.DEBUG)


# @bot.message_handler(func=lambda message: True, content_types=['text'])
# def info_message(message):
#     msg = message.text.lower()
#     if message.chat.type == 'group':
#         msg = ' '.join(msg.split(" ")[1:])
#     if msg == 'get id':
#         bot.send_message(message.chat.id, message.chat.id)
#
#
# def morning_message():
#     bot.send_message(chat_id='@', text='Доброе утро!')
#
#
# schedule.every().day.at("20:56").do(morning_message)
# while True:
#     schedule.run_pending()
#     time.sleep(1)
#

@bot.message_handler(commands=['benleave', 'benfuckoff'])
def handler_leave(message):
    bot.leave_chat(message.chat.id)


@bot.message_handler(commands=['chemistry'])
def play_chemistry(message):
    markup = types.InlineKeyboardMarkup()
    yellow_button = types.InlineKeyboardButton(text='Желтая☀', callback_data='ylw')
    green_button = types.InlineKeyboardButton(text='Зеленая🌳', callback_data='gr')
    light_blue_button = types.InlineKeyboardButton(text='Голубая💦', callback_data='lb')
    pink_button = types.InlineKeyboardButton(text='Розовая🎀', callback_data='pnk')
    blue_button = types.InlineKeyboardButton(text='Синяя💙', callback_data='bl')
    markup.add(yellow_button, green_button, light_blue_button, pink_button, blue_button)
    bot.send_message(message.chat.id, 'Выбери первую пробирку', reply_markup=markup)


def next_chemistry(message):
    bot.edit_message_reply_markup(chat_id=message.chat.id, message_id=message.message_id - 1, reply_markup=None)


@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call):
    if call.message:
        if call.data == 'ylw':
            bot.edit_message_text(chat_id=call.message.chat.id, text="Вы выбрали желтую пробирку☀",
                                  message_id=call.message.message_id, reply_markup=None)
            markup = types.InlineKeyboardMarkup()
            green_button = types.InlineKeyboardButton(text='Зеленая🌳', callback_data='y_green')
            light_blue_button = types.InlineKeyboardButton(text='Голубая💦', callback_data='y_lightblue')
            pink_button = types.InlineKeyboardButton(text='Розовая🎀', callback_data='y_pink')
            blue_button = types.InlineKeyboardButton(text='Синяя💙', callback_data='y_blue')
            markup.add(green_button, light_blue_button, pink_button, blue_button)
            bot.send_message(chat_id=call.message.chat.id, text='Выберите вторую пробирку', reply_markup=markup)
        elif call.data == 'gr':
            bot.edit_message_text(chat_id=call.message.chat.id, text="Вы выбрали зеленую пробирку🌳",
                                  message_id=call.message.message_id, reply_markup=None)
            markup = types.InlineKeyboardMarkup()
            yellow_button = types.InlineKeyboardButton(text='Желтая☀', callback_data='g_yellow')
            light_blue_button = types.InlineKeyboardButton(text='Голубая💦', callback_data='g_lightblue')
            pink_button = types.InlineKeyboardButton(text='Розовая🎀', callback_data='g_pnk')
            blue_button = types.InlineKeyboardButton(text='Синяя💙', callback_data='g_blue')
            markup.add(yellow_button, light_blue_button, pink_button, blue_button)
            bot.send_message(chat_id=call.message.chat.id, text='Выберите вторую пробирку', reply_markup=markup)
        elif call.data == 'lb':
            bot.edit_message_text(chat_id=call.message.chat.id, text="Вы выбрали голубую пробирку💦",
                                  message_id=call.message.message_id, reply_markup=None)
            markup = types.InlineKeyboardMarkup()
            yellow_button = types.InlineKeyboardButton(text='Желтая☀', callback_data='lb_ylw')
            green_button = types.InlineKeyboardButton(text='Зеленая🌳', callback_data='lb_gr')
            pink_button = types.InlineKeyboardButton(text='Розовая🎀', callback_data='lb_pnk')
            blue_button = types.InlineKeyboardButton(text='Синяя💙', callback_data='lb_bl')
            markup.add(yellow_button, green_button, pink_button, blue_button)
            bot.send_message(chat_id=call.message.chat.id, text='Выберите вторую пробирку', reply_markup=markup)
        elif call.data == 'pnk':
            bot.edit_message_text(chat_id=call.message.chat.id, text="Вы выбрали розовую пробирку🎀",
                                  message_id=call.message.message_id, reply_markup=None)
            markup = types.InlineKeyboardMarkup()
            yellow_button = types.InlineKeyboardButton(text='Желтая☀', callback_data='p_ylw')
            green_button = types.InlineKeyboardButton(text='Зеленая🌳', callback_data='p_gr')
            light_blue_button = types.InlineKeyboardButton(text='Голубая💦', callback_data='p_lb')
            blue_button = types.InlineKeyboardButton(text='Синяя💙', callback_data='p_bl')
            markup.add(yellow_button, green_button, light_blue_button, blue_button)
            bot.send_message(chat_id=call.message.chat.id, text='Выберите вторую пробирку', reply_markup=markup)
        elif call.data == 'bl':
            bot.edit_message_text(chat_id=call.message.chat.id, text="Вы выбрали синюю пробирку💙",
                                  message_id=call.message.message_id, reply_markup=None)
            markup = types.InlineKeyboardMarkup()
            yellow_button = types.InlineKeyboardButton(text='Желтая☀', callback_data='bl_ylw')
            green_button = types.InlineKeyboardButton(text='Зеленая🌳', callback_data='bl_gr')
            light_blue_button = types.InlineKeyboardButton(text='Голубая💦', callback_data='bl_lb')
            pink_button = types.InlineKeyboardButton(text='Розовая🎀', callback_data='bl_pnk')
            markup.add(yellow_button, green_button, light_blue_button, pink_button)
            bot.send_message(chat_id=call.message.chat.id, text='Выберите вторую пробирку', reply_markup=markup)
        elif call.data == 'p_gr':
            bot.edit_message_text(chat_id=call.message.chat.id, text="Вы выбрали зеленую пробирку🌳",
                                  message_id=call.message.message_id, reply_markup=None)
            img = open('chemistry/p_gr.gif', 'rb')
            bot.send_animation(chat_id=call.message.chat.id, animation=img)
        elif call.data == 'y_green':
            bot.edit_message_text(chat_id=call.message.chat.id, text="Вы выбрали зеленую пробирку🌳",
                                  message_id=call.message.message_id, reply_markup=None)
            img = open('chemistry/y_gr.gif', 'rb')
            bot.send_animation(chat_id=call.message.chat.id, animation=img)
        elif call.data == 'bl_gr':
            bot.edit_message_text(chat_id=call.message.chat.id, text="Вы выбрали зеленую пробирку🌳",
                                  message_id=call.message.message_id, reply_markup=None)
            img = open('chemistry/bl_gr.gif', 'rb')
            bot.send_animation(chat_id=call.message.chat.id, animation=img)
        elif call.data == 'lb_gr':
            bot.edit_message_text(chat_id=call.message.chat.id, text="Вы выбрали зеленую пробирку🌳",
                                  message_id=call.message.message_id, reply_markup=None)
            img = open('chemistry/lb_gr.gif', 'rb')
            bot.send_animation(chat_id=call.message.chat.id, animation=img)
        elif call.data == 'p_ylw':
            bot.edit_message_text(chat_id=call.message.chat.id, text="Вы выбрали желтую пробирку☀",
                                  message_id=call.message.message_id, reply_markup=None)
            img = open('chemistry/p_ylw.gif', 'rb')
            bot.send_animation(chat_id=call.message.chat.id, animation=img)
        elif call.data == 'g_yellow':
            bot.edit_message_text(chat_id=call.message.chat.id, text="Вы выбрали желтую пробирку☀",
                                  message_id=call.message.message_id, reply_markup=None)
            img = open('chemistry/g_ylw.gif', 'rb')
            bot.send_animation(chat_id=call.message.chat.id, animation=img)
        elif call.data == 'lb_ylw':
            bot.edit_message_text(chat_id=call.message.chat.id, text="Вы выбрали желтую пробирку☀",
                                  message_id=call.message.message_id, reply_markup=None)
            img = open('chemistry/lb_ylw.gif', 'rb')
            bot.send_animation(chat_id=call.message.chat.id, animation=img)
        elif call.data == 'bl_ylw':
            bot.edit_message_text(chat_id=call.message.chat.id, text="Вы выбрали желтую пробирку☀",
                                  message_id=call.message.message_id, reply_markup=None)
            img = open('chemistry/bl_ylw.gif', 'rb')
            bot.send_animation(chat_id=call.message.chat.id, animation=img)
        elif call.data == 'p_lb':
            bot.edit_message_text(chat_id=call.message.chat.id, text="Вы выбрали голубую пробирку💦",
                                  message_id=call.message.message_id, reply_markup=None)
            img = open('chemistry/p_lb.gif', 'rb')
            bot.send_animation(chat_id=call.message.chat.id, animation=img)
        elif call.data == 'y_lightblue':
            bot.edit_message_text(chat_id=call.message.chat.id, text="Вы выбрали голубую пробирку💦",
                                  message_id=call.message.message_id, reply_markup=None)
            img = open('chemistry/y_lb.gif', 'rb')
            bot.send_animation(chat_id=call.message.chat.id, animation=img)
        elif call.data == 'g_lightblue':
            bot.edit_message_text(chat_id=call.message.chat.id, text="Вы выбрали голубую пробирку💦",
                                  message_id=call.message.message_id, reply_markup=None)
            img = open('chemistry/g_lb.gif', 'rb')
            bot.send_animation(chat_id=call.message.chat.id, animation=img)
        elif call.data == 'bl_lb':
            bot.edit_message_text(chat_id=call.message.chat.id, text="Вы выбрали голубую пробирку💦",
                                  message_id=call.message.message_id, reply_markup=None)
            img = open('chemistry/bl_lb.gif', 'rb')
            bot.send_animation(chat_id=call.message.chat.id, animation=img)
        elif call.data == 'p_bl':
            bot.edit_message_text(chat_id=call.message.chat.id, text="Вы выбрали синюю пробирку💙",
                                  message_id=call.message.message_id, reply_markup=None)
            img = open('chemistry/p_bl.gif', 'rb')
            bot.send_animation(chat_id=call.message.chat.id, animation=img)
        elif call.data == 'y_blue':
            bot.edit_message_text(chat_id=call.message.chat.id, text="Вы выбрали синюю пробирку💙",
                                  message_id=call.message.message_id, reply_markup=None)
            img = open('chemistry/y_bl.gif', 'rb')
            bot.send_animation(chat_id=call.message.chat.id, animation=img)
        elif call.data == 'g_blue':
            bot.edit_message_text(chat_id=call.message.chat.id, text="Вы выбрали синюю пробирку💙",
                                  message_id=call.message.message_id, reply_markup=None)
            img = open('chemistry/g_bl.gif', 'rb')
            bot.send_animation(chat_id=call.message.chat.id, animation=img)
        elif call.data == 'lb_bl':
            bot.edit_message_text(chat_id=call.message.chat.id, text="Вы выбрали синюю пробирку💙",
                                  message_id=call.message.message_id, reply_markup=None)
            img = open('chemistry/lb_bl.gif', 'rb')
            bot.send_animation(chat_id=call.message.chat.id, animation=img)
        elif call.data == 'lb_pnk':
            bot.edit_message_text(chat_id=call.message.chat.id, text="Вы выбрали розовую пробирку🎀",
                                  message_id=call.message.message_id, reply_markup=None)
            img = open('chemistry/lb_pnk.gif', 'rb')
            bot.send_animation(chat_id=call.message.chat.id, animation=img)
        elif call.data == 'bl_pnk':
            bot.edit_message_text(chat_id=call.message.chat.id, text="Вы выбрали розовую пробирку🎀",
                                  message_id=call.message.message_id, reply_markup=None)
            img = open('chemistry/bl_pnk.gif', 'rb')
            bot.send_animation(chat_id=call.message.chat.id, animation=img)
        elif call.data == 'g_pnk':
            bot.edit_message_text(chat_id=call.message.chat.id, text="Вы выбрали розовую пробирку🎀",
                                  message_id=call.message.message_id, reply_markup=None)
            img = open('chemistry/g_pnk.gif', 'rb')
            bot.send_animation(chat_id=call.message.chat.id, animation=img)
        elif call.data == 'y_pink':
            bot.edit_message_text(chat_id=call.message.chat.id, text="Вы выбрали розовую пробирку🎀",
                                  message_id=call.message.message_id, reply_markup=None)
            img = open('chemistry/y_pnk.gif', 'rb')
            bot.send_animation(chat_id=call.message.chat.id, animation=img)


@bot.message_handler(commands=['start'])
def handler_start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton('👋 Поздороваться')
    btn2 = types.KeyboardButton('🤷‍♀️🤷‍♂️Создатели')
    markup.add(btn1, btn2)
    img = open('answers/start.gif', 'rb')
    text = 'Привет, {0.first_name}! Меня зовут Бен. Спроси у меня что-нибудь (/talk <текст>)'.format(message.from_user)
    bot.send_animation(message.chat.id, img, caption=text, reply_markup=markup)


# @bot.message_handler(commands=['games' , 'game'])
# def handler_games(message):
#     bot.send_game(message.chat.id, '')
@bot.message_handler(commands=['talk'])
def handler_talk(message):
    message.text = message.text.lower()
    if 'гавс' in message.text:
        random.seed(time.time())
        img = open(random.choice(constants.benGenGavs_IMG), 'rb')
        bot.send_photo(message.chat.id, img, caption=constants.benTotalGenGavs())
    elif '?' in message.text:
        answer, photo_path = constants.benTotalAnswer()
        img = open(photo_path, 'rb')
        bot.send_animation(message.chat.id, img, caption=answer)
    else:
        img = open('answers/stop.gif', 'rb')
        bot.send_animation(message.chat.id, img, caption=constants.benTotalPhrase())


@bot.message_handler(content_types=['text'])
def handler_text(message):
    message.text = message.text.lower()
    if ('привет' in message.text) or ('поздороваться' in message.text):
        bot.send_message(message.chat.id, constants.benTotalGreetings())
    # elif (('как') and (('дела') or ('ты')) in message.text):
    #     answer, photo_path = constants.benTotalMood()
    #     bot.send_animation(message.chat.id)
    elif ('создатели' in message.text) or ('разработчики' in message.text) or ('создали' in message.text) \
            or ('создатель' in message.text) or ('разработал' in message.text) or ('создал' in message.text):
        markup = types.InlineKeyboardMarkup()
        button_elena = types.InlineKeyboardButton('Лена', url='https://vk.com/lenokpushok')
        markup.add(button_elena)
        button_boris = types.InlineKeyboardButton('Боря', url='https://vk.com/b.keselman')
        markup.add(button_boris)
        bot.send_media_group(message.chat.id, [
            bot.send_message(message.chat.id, 'Меня создали два прекрасных человека - Елена и Борис! '
                                              'Вот смотрите, какие они милые', reply_markup=markup),
            telebot.types.InputMediaPhoto(open('Elena.jpg', 'rb')),
            telebot.types.InputMediaPhoto(open('Boris.jpg', 'rb')),
        ])


if __name__ == '__main__':
    bot.polling(non_stop=True)
