# This is a sample Python script.

# Press Mayús+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


import boto3
from flask import Flask, request,jsonify
import joblib

app = Flask(__name__)
s3 = boto3.resource('s3')
s3.meta.client.download_file('creditdata2080', 'modelo/modelrf.joblib', 'modelrf.joblib')
model = joblib.load('modelrf.joblib')

@app.route("/")
def index():
    return "Hi_Flask"

@app.route("/predict", methods=['POST'])
def predict():
    request_data = request.get_json()
    age = request_data["age"]
    sex = request_data["sex"]
    credit_amount = request_data["credit_amount"]
    duration = request_data["duration"]
    purpose = request_data["purpose"]
    housing = request_data["housing"]
    prediction = model.predict([[age, credit_amount, duration,sex,purpose,housing]])
    return jsonify({"prediction": prediction.tolist()})


if __name__ == '__main__':
    app.run(host='0.0.0.0')
