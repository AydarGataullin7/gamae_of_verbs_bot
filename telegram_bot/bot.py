import logging
import os
from telegram import Update
from telegram.ext import Updater, CallbackContext, CommandHandler, MessageHandler, Filters
from google.cloud import dialogflow_v2 as dialogflow
from dotenv import load_dotenv

def start(update: Update, context: CallbackContext):
    context.bot.send_message(
        chat_id=update.effective_chat.id, text="Здравствуйте!")


def echo(update: Update, context: CallbackContext):
    user_text = update.message.text
    session_id = str(update.effective_chat.id)
    reply = detect_intent(PROJECT_ID, session_id, user_text)
    context.bot.send_message(chat_id=update.effective_chat.id, text=reply)


def detect_intent(project_id, session_id, text):
    client = dialogflow.SessionsClient()
    session = client.session_path(project_id, session_id)
    text = dialogflow.TextInput(text=text, language_code="ru")
    query_input = dialogflow.QueryInput(text=text)
    response = client.detect_intent(
        request={'session': session, 'query_input': query_input})
    response_text = response.query_result.fulfillment_text
    return response_text


if __name__ == '__main__':
    load_dotenv()    
    updater = Updater(token=os.getenv("TG_BOT_TOKEN"))
    PROJECT_ID = os.getenv("PROJECT_ID")
    dispatcher = updater.dispatcher
    logging.basicConfig(
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')

    dispatcher.add_handler(CommandHandler('start', start))
    dispatcher.add_handler(MessageHandler(
        Filters.text & ~Filters.command, echo))

    updater.start_polling()
    updater.idle()
