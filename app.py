import os
import numpy as np
import flask
import pickle
from flask import Flask, render_template, request

app=Flask(__name__)


def valuePredictor(to_predict_list):
    to_predict = np.array(to_predict_list).reshape(1, 19)
    loaded_model = pickle.load(open("./model/final_model.pkl", "rb"))
    result = loaded_model.predict(to_predict)
    return result[0]

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/dataset')
def dataset():
    return render_template('tentang_dataset.html')

@app.route('/predict')
def predict():
    return render_template('predict.html')

@app.route('/result',methods = ['POST'])
def result():
    if request.method == 'POST':
        to_predict_list = request.form.to_dict()
        to_predict_list=list(to_predict_list.values())
        to_predict_list = list(map(float, to_predict_list))
        result = valuePredictor(to_predict_list)
    
    return render_template("result.html", result=result)

if __name__ == "__main__":
    app.debug=False
    app.run()