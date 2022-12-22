
import os

from dotenv import load_dotenv
from handlers import answer_text, cat_seda, new_cats, wake_up
from telegram.ext import CommandHandler, Filters, MessageHandler, Updater

load_dotenv()

secret_token = os.getenv('TOKEN')


def main():
    updater = Updater(token=secret_token)
    updater.dispatcher.add_handler(MessageHandler(Filters.regex('^(Показать котика)$'), new_cats))
    updater.dispatcher.add_handler(MessageHandler(Filters.regex('^(Показать Сэду)$'), cat_seda))
    updater.dispatcher.add_handler(CommandHandler('start', wake_up))
    updater.dispatcher.add_handler(MessageHandler(Filters.text, answer_text))

    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    main()
