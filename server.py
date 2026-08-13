"""
This module implements a Flask web server for the Emotion Detection Application.
"""

from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detector")

@app.route("/emotionDetector")
def emt_detector():
    """
    Analyze the text provided in the request and returns the dominant emotion.
    """
    text_to_analyze = request.args.get('textToAnalyze')
    response = emotion_detector(text_to_analyze)
    if response['dominant_emotion'] is None:
        return "Invalid text. Please try again"

    emotion = response['dominant_emotion']
    score = response[emotion]
    return f"The given text has been identified as {emotion} with a score of {score}."

@app.route("/")
def render_index_page():
    """
    Renders the main index page for the application.
    """
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
    