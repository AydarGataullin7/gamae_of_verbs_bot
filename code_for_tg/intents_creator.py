import json
import os
import time
from dotenv import load_dotenv
from google.cloud import dialogflow_v2 as dialogflow

load_dotenv()
project_id = os.getenv('PROJECT_ID')

with open('questions.json', 'r', encoding='utf-8') as file:
    questions = json.load(file)


def create_intent(project_id, display_name, training_phrases, answer_text):
    intents_client = dialogflow.IntentsClient()
    agents_client = dialogflow.AgentsClient()
    
    parent = agents_client.agent_path(project_id)

    training_phrases_list = []
    for phrase in training_phrases:
        training_phrase = {
            "type": "EXAMPLE",
            "parts": [{"text": phrase}]
        }
        training_phrases_list.append(training_phrase)

    intent = {
        "display_name": display_name,
        "training_phrases": training_phrases_list,
        "messages": [{
            "text": {"text": [answer_text]}
        }]
    }
    response = intents_client.create_intent(
            request={
                'parent': parent, 
                'intent': intent,
                'language_code': 'ru'
            }
        )

if __name__ == "__main__":
    for topic_name, topic_data in questions.items():
        create_intent(
            project_id=project_id,
            display_name=topic_name,
            training_phrases=topic_data['questions'],
            answer_text=topic_data['answer']
        )
    print("Готово! Проверьте агента в DialogFlow.")
