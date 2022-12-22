from glob import glob
from random import choice

from telegram import ReplyKeyboardMarkup
from utils import get_new_image, get_smile


def answer_text(update, context):
    context.user_data['emoji'] = get_smile(context.user_data)
    text = 'Привет, я KittyBot! {} Я показываю самых милых котиков! Нажми на --> /start'.format(context.user_data['emoji'])
    chat = update.effective_chat
    context.bot.send_message(chat_id=chat.id, text=text)


def new_cats(update, context):
    text = 'Как славно, что Вы захотели посмотреть на милого котика'
    chat = update.effective_chat
    context.bot.send_message(chat_id=chat.id, text=text)
    context.bot.send_photo(chat.id, get_new_image())


def wake_up(update, context):
    chat = update.effective_chat
    name = update.message.chat.first_name
    context.user_data['emoji'] = get_smile(context.user_data)
    button = ReplyKeyboardMarkup([['Показать котика', 'Показать Сэду']], resize_keyboard=True)
    context.bot.send_message(
        chat_id=chat.id,
        text='Привет, {}. Посмотри, какого котика я тебе нашёл {}'.format(name, context.user_data['emoji']),
        reply_markup=button
        )
    context.bot.send_photo(chat.id, get_new_image())


def new_cat(update, context):
    chat = update.effective_chat
    context.bot.send_photo(chat.id, get_new_image())


def cat_seda(update, context):
    chat = update.effective_chat
    cat_photo_list = glob('images/*.jp*g')
    cat_foto_filename = choice(cat_photo_list)
    context.bot.send_photo(chat.id, photo=open(cat_foto_filename, 'rb'))
