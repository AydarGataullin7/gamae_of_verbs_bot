import logging
import os
from telegram import Update
from telegram.ext import Updater, CallbackContext, CommandHandler, MessageHandler, Filters
from dotenv import load_dotenv
from dialogflow_client import detect_intent


def start(update: Update, context: CallbackContext):
    context.bot.send_message(
        chat_id=update.effective_chat.id, text="Здравствуйте!")


def handle_message(update: Update, context: CallbackContext):
    user_text = update.message.text
    session_id = str(update.effective_chat.id)
    reply, _ = detect_intent(PROJECT_ID, session_id, user_text)
    context.bot.send_message(chat_id=update.effective_chat.id, text=reply)


if __name__ == '__main__':
    load_dotenv()
    PROJECT_ID = os.getenv('PROJECT_ID')
    updater = Updater(token=os.getenv("TG_BOT_TOKEN"))
    dispatcher = updater.dispatcher
    logging.basicConfig(
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')

    dispatcher.add_handler(CommandHandler('start', start))
    dispatcher.add_handler(MessageHandler(
        Filters.text & ~Filters.command, handle_message))

    updater.start_polling()
    updater.idle()
