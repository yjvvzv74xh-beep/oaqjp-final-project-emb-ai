from flask import Flask, render_template, request 
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detector") 

@app.route("/emotionDetector")
def emt_detector():
    text_to_analyze = request.args.get('textToAnalyze')
    response = emotion_detector(text_to_analyze)
    
    if response['dominant_emotion'] is None:
        return "Invalid text. Please try again"

    emotion = response['dominant_emotion'] 
    score = response[emotion] 
    return "The given text has been identified as {} with a score of {}.".format(emotion, score)

@app.route("/")
def render_index_page():
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)