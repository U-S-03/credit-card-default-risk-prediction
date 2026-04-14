from flask import Flask, render_template, jsonify, request, send_file
from src.exception import CustomException
from src.logger import logging as lg
import os,sys

from src.pipeline.train_pipeline import TraininingPipeline
from src.pipeline.predict_pipeline import PredictionPipeline

app = Flask(__name__)

# HOME -> show upload page
@app.route("/")
def home():
    return render_template("upload_file.html")


# TRAIN ROUTE
@app.route("/train")
def train():
    try:
        train_pipeline = TraininingPipeline()
        train_pipeline.run_pipeline()
        return "Training Completed"
    except Exception as e:
        return str(e)


# PREDICT ROUTE
@app.route('/predict', methods=['POST'])
def predict():
    try:
        file = request.files.get("file")

        if file is None or file.filename == "":
            return "No file selected"

        prediction_pipeline = PredictionPipeline(request)
        prediction_file_path = prediction_pipeline.run_pipeline()

        return send_file(prediction_file_path, as_attachment=True)

    except Exception as e:
        print(e)
        return str(e)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=False)