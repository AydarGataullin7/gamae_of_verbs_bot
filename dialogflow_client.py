from google.cloud import dialogflow_v2 as dialogflow


def detect_intent(project_id, session_id, text):
    client = dialogflow.SessionsClient()
    session = client.session_path(project_id, session_id)
    text_input = dialogflow.TextInput(text=text, language_code="ru")
    query_input = dialogflow.QueryInput(text=text_input)
    response = client.detect_intent(
        request={'session': session, 'query_input': query_input}
    )
    response_text = response.query_result.fulfillment_text
    is_fallback = response.query_result.intent.is_fallback
    return response_text, is_fallback