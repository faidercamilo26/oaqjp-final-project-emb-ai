import requests

def emotion_detector(text_to_analyze):
    
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    input = { "raw_document": { "text": text_to_analyze } }
    
    response_api =requests.post(url, headers=headers, json=input)
    
    response_json = response_api.json()
    
    emotions_data = response_json['emotionPredictions'][0]['emotion']

    emotions = {
        'anger': emotions_data['anger'],
        'disgust': emotions_data['disgust'],
        'fear': emotions_data['fear'],
        'joy': emotions_data['joy'],
        'sadness': emotions_data['sadness']
    }

    dominant_emotion = max(emotions, key=emotions.get)
    
    emotions['dominant_emotion'] = dominant_emotion

    return emotions