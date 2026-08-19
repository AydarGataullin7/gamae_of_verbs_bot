import random
import vk_api
import os
from dotenv import load_dotenv
from vk_api.longpoll import VkLongPoll, VkEventType
from dialogflow_client import detect_intent


def handle_message(event, vk_api, project_id):
    session_id = f"vk_{event.user_id}"
    reply, is_fallback = detect_intent(project_id, session_id, event.text)
    if not is_fallback:
        vk_api.messages.send(
            user_id=event.user_id,
            message=reply,
            random_id=random.randint(1, 1000)
        )


if __name__ == '__main__':
    load_dotenv()
    project_id = os.getenv('PROJECT_ID')
    vk_session = vk_api.VkApi(token=os.getenv("VK_TOKEN"))
    vk_api = vk_session.get_api()
    longpoll = VkLongPoll(vk_session)
    for event in longpoll.listen():
        if event.type == VkEventType.MESSAGE_NEW and event.to_me:
            handle_message(event, vk_api, project_id)
