import random
import vk_api
import os
from google.cloud import dialogflow_v2 as dialogflow
from dotenv import load_dotenv
from vk_api.longpoll import VkLongPoll, VkEventType

load_dotenv()
project_id = os.getenv('PROJECT_ID')


def echo(event, vk_api, project_id):
    session_id = str(event.user_id)
    reply, is_fallback = detect_intent(project_id, session_id, event.text)
    if not is_fallback:
        vk_api.messages.send(
            user_id=event.user_id,
            message=reply,
            random_id=random.randint(1, 1000)
        )


def detect_intent(project_id, session_id, text):
    client = dialogflow.SessionsClient()
    session = client.session_path(project_id, session_id)
    text = dialogflow.TextInput(text=text, language_code="ru")
    query_input = dialogflow.QueryInput(text=text)
    response = client.detect_intent(
        request={'session': session, 'query_input': query_input})
    response_text = response.query_result.fulfillment_text
    is_fallback = response.query_result.intent.is_fallback
    return response_text, is_fallback


if __name__ == '__main__':
    vk_session = vk_api.VkApi(token=os.getenv("VK_TOKEN"))
    vk_api = vk_session.get_api()
    longpoll = VkLongPoll(vk_session)
    for event in longpoll.listen():
        if event.type == VkEventType.MESSAGE_NEW and event.to_me:
            echo(event, vk_api, project_id)
