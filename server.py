from flask import Flask, request, render_template
from EmotionDetection.emotion_detection import emotion_detector
app = Flask("__name__", template_folder='/home/project/final_project/oaqjp-final-project-emb-ai/templates')

@app.route("/emotionDetector")
def emotion_detection():
    text_to_analyse = request.args.get('textToAnalyze')
    response = emotion_detector(text_to_analyse)
    anger = response['anger']
    disgust = response['disgust']
    fear = response['fear']
    joy = response['joy']
    sadness = response['sadness']
    dominant_emotion = response['dominant_emotion']
    response_str = """For the given statement, the system response is 'anger': {} , 'disgust': {} , 'fear': {} , 'joy': {}  
    and 'sadness': {}. The dominant emotion is {}.""".format(anger, disgust, fear, joy, sadness, dominant_emotion)
    if dominant_emotion == None:
        return "Invalid text! Please try again!"
    
    
    return response_str



@app.route("/")
def render_index_page():
    
    return render_template('index.html')

if __name__ == '__main__':
5000    app.run(host="0.0.0.0", port=8080)