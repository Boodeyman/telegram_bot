import telebot
import webbrowser
from telebot import types
import sqlite3

bot = telebot.TeleBot('6597029609:AAHkglleSuDyZz4jtyi0y2glr3QkpU64aPc')


@bot.message_handler(commands = ['start'])
def start(message):
    bot.send_message(message.chat.id, 'Здравствуйте! Как я могу к Вам обращаться?')
    bot.register_next_step_handler(message, main)

def main(message):
    name = message.text.strip()
    markup = types.ReplyKeyboardMarkup()
    btn1 = types.KeyboardButton('Оформить заем')
    markup.row(btn1)
    btn2 = types.KeyboardButton('Перейти на сайт')
    btn3 = types.KeyboardButton('Ознакомиться с текущими акциями')
    markup.row(btn2, btn3)
    bot.send_message(message.chat.id, f'Очень приятно, {name}! Что Вас интересует?', reply_markup = markup)
    bot.register_next_step_handler(message, on_click)

def on_click(message):
    if message.text.lower() == 'оформить заем':
        bot.send_message(message.chat.id, 'Прошу отправить фото паспорта')
        @bot.message_handler(content_types = ['photo'])
        def photo(message):
            markup = types.InlineKeyboardMarkup()
            btn1 = types.InlineKeyboardButton('Перейти на сайт', url = 'https://bzaem.com')
            btn2 = types.InlineKeyboardButton('Изменить фото', callback_data = 'delete')
            markup.row(btn1, btn2)
            bot.send_message(message.chat.id, 'Ожидаем ответа оператора. А пока, Вы можете ознакомиться с нашими акциями', reply_markup = markup)
    elif message.text.lower() == 'перейти на сайт':
        webbrowser.open('https://bzaem.com')
    elif message.text.lower() == 'ознакомиться с текущими акциями':
        webbrowser.open('https://bzaem.com')


@bot.callback_query_handler(func = lambda callback: True)
def callback_message(callback):
    callback.data == 'delite'
    bot.delete_message(callback.message.chat.id, callback.message.message_id)
    bot.delete_message(callback.message.chat.id, callback.message.message_id -1)

bot.polling(none_stop=True)

'''@bot.message_handler(commands = ['site', 'website'])
def site(message):
    webbrowser.open('https://bzaem.com')'''

'''@bot.message_handler()
def info(message):
    markup = types.ReplyKeyboardMarkup()
    btn1 = types.KeyboardButton('Оформить заем', callback_data = 'start')
    markup.row(btn1)
    btn2 = types.KeyboardButton('Перейти на сайт', url='https://bzaem.com')
    btn3 = types.KeyboardButton('Ознакомиться с текущими акциями', url='https://bzaem.com')
    markup.row(btn2, btn3)
    bot.send_message(message.chat.id, f'Здравствуйте, {message.from_user.first_name}! Что Вас интересует?')'''

'''
    conn = sqlite3.connect('BananzaBot.sql')
    cur = conn.cursor()
    cur.execute('CREATE TABLE IF NOT EXISTS users (id int auto_increment primary key, name varchar(50), pasport varchar(50))')
    conn.commit()
    cur.close()
    conn.close()
    bot.send_message(message.chat.id, 'Как я могу к Вам обращатсья?')
    bot.register_next_step_handler(message, user_name)

def user_name(message):
    global name
    name = message.text.strip()
    bot.send_message(message.chat.id, 'Паспорт!')
    bot.register_next_step_handler(message, user_pasport)

def user_pasport(message):
    pasport = message.text.strip()
    conn = sqlite3.connect('BananzaBot.sql')
    cur = conn.cursor()
    cur.execute("INSERT INTO users (name, pasport) VALUES('%s', '%s')" % (name, pasport))
    conn.commit()
    cur.close()
    conn.close()
    bot.send_message(message.chat.id, 'Отлично!')
'''