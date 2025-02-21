import requests, json

def emotion_detector(text_to_analyse):
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    myobj = { "raw_document": { "text": text_to_analyse } }
    response = requests.post(url, json = myobj, headers=header) 
    status_code = response.status_code
    
    emotion_dict = {}

    if status_code == 200:
        formatted_response = json.loads(response.text)
        anger = formatted_response["emotionPredictions"][0]['emotion']["anger"]
        disgust = formatted_response["emotionPredictions"][0]['emotion']["disgust"]
        fear = formatted_response["emotionPredictions"][0]['emotion']["fear"]
        joy = formatted_response['emotionPredictions'][0]['emotion']['joy']
        sadness = formatted_response['emotionPredictions'][0]['emotion']['sadness']
    
        emotion_dict = formatted_response['emotionPredictions'][0]['emotion']

        dominant_emotion = max(emotion_dict, key=emotion_dict.get)
        dominant_value = emotion_dict[dominant_emotion]

        emotion_dict['dominant_emotion'] = dominant_emotion[:]

    elif status_code == 400:
        emotion_dict['anger'] = None
        emotion_dict['disgust'] = None
        emotion_dict['fear'] = None
        emotion_dict['joy'] = None
        emotion_dict['sadness'] = None
        emotion_dict['dominant_emotion'] = None
        return emotion_dict

    return emotion_dict
    

    #return({"anger": anger, "disgust": disgust, "fear": fear, "joy": joy, "sadness": sadness,  "dominant_emotion": dominant_emotion } )




