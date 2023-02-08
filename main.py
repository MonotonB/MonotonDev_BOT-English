import telebot
import os
from telebot import types
from dotenv import load_dotenv

load_dotenv('token.env')

TELEGRAM_BOT_TOKEN = os.getenv('BOTTOKEN')

bot = telebot.TeleBot(TELEGRAM_BOT_TOKEN)


@bot.message_handler(content_types=['text'])
def start(message):
    if message.text == '/start':
        keyboard = types.InlineKeyboardMarkup()
        button_github = types.InlineKeyboardButton(text='GitHub page', callback_data='github')
        button_projects = types.InlineKeyboardButton(text='Projects', callback_data='projects')
        keyboard.add(button_github, button_projects)
        bot.send_message(message.from_user.id, 'Hi! Choose what you want to do?', reply_markup=keyboard)


def projects(message):
    if message.text == '/projects':
        keyboard = types.InlineKeyboardMarkup()
        button_link = types.InlineKeyboardButton(text='MonotonDev_BOT', callback_data='projects-monotondev_bot')
        button_github = types.InlineKeyboardButton(text='GitHub page', callback_data='github')
        button_back = types.InlineKeyboardButton(text='Back to menu', callback_data='back-to-menu')
        keyboard.add(button_link, button_github, button_back)
        bot.send_message(message.from_user.id, 'Select project.',
                         reply_markup=keyboard)


def github(message):
    if message.text == '/github':
        keyboard = types.InlineKeyboardMarkup()
        button_link = types.InlineKeyboardButton(text='GitHub page', callback_data='github-link')
        button_back = types.InlineKeyboardButton(text='Back to menu', callback_data='back-to-menu')
        keyboard.add(button_link, button_back)
        bot.send_message(message.from_user.id, 'To get a link to GitHub, click.',
                         reply_markup=keyboard)


@bot.callback_query_handler(func=lambda call: True)
def callback(call):
    if call.data == 'projects':
        keyboard = types.InlineKeyboardMarkup()
        button_link = types.InlineKeyboardButton(text='MonotonDev_BOT', callback_data='projects-monotondev_bot')
        button_github = types.InlineKeyboardButton(text='GitHub page', callback_data='github')
        button_back = types.InlineKeyboardButton(text='Back to menu.', callback_data='back-to-menu')
        keyboard.add(button_link, button_github, button_back)
        bot.send_message(call.message.chat.id, 'Select project.',
                         reply_markup=keyboard)
    elif call.data == 'github':
        keyboard = types.InlineKeyboardMarkup()
        button_link = types.InlineKeyboardButton(text='GitHub page', callback_data='github-link')
        button_back = types.InlineKeyboardButton(text='Back to menu', callback_data='back-to-menu')
        keyboard.add(button_link, button_back)
        bot.send_message(call.message.chat.id, 'To get a link to GitHub, click.',
                         reply_markup=keyboard)
    elif call.data == 'back-to-menu':
        keyboard = types.InlineKeyboardMarkup()
        button_github = types.InlineKeyboardButton(text='Страница GitHub', callback_data='github')
        button_projects = types.InlineKeyboardButton(text='Проекты', callback_data='projects')
        keyboard.add(button_github, button_projects)
        bot.send_message(call.message.chat.id, 'Hi! Choose what you want to do?', reply_markup=keyboard)
    elif call.data == 'github-link':
        bot.send_message(call.message.chat.id, 'GitHub - https://github.com/MonotonB')
        keyboard = types.InlineKeyboardMarkup()
        button_link = types.InlineKeyboardButton(text='GitHub page', callback_data='github-link')
        button_back = types.InlineKeyboardButton(text='Back to menu.', callback_data='back-to-menu')
        keyboard.add(button_link, button_back)
        bot.send_message(call.message.chat.id, 'To get a link to GitHub, click.',
                         reply_markup=keyboard)

    elif call.data == 'projects-monotondev_bot':
        bot.send_message(call.message.chat.id, 'MonotonDev_BOT - https://github.com/MonotonB/MonotonDev_BOT')
        keyboard = types.InlineKeyboardMarkup()
        button_link = types.InlineKeyboardButton(text='MonotonDev_BOT', callback_data='projects-monotondev_bot')
        button_github = types.InlineKeyboardButton(text='GitHub page', callback_data='github')
        button_back = types.InlineKeyboardButton(text='Back to menu.', callback_data='back-to-menu')
        keyboard.add(button_link, button_github, button_back)
        bot.send_message(call.message.chat.id, 'Select project.',
                         reply_markup=keyboard)


bot.polling(none_stop=True, interval=0)
