import os
import numpy as np
import flask
import pickle
from flask import Flask, render_template, request

app=Flask(__name__)

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/dataset')
def dataset():
    return render_template('tentang_dataset.html')

@app.route('/tentang-kami')
def tentang_kami():
    return render_template('tentang_kami.html')

@app.route('/predict')
def predict():
    return render_template('predict.html')

def ValuePredictor(to_predict_list):
    to_predict = np.array(to_predict_list).reshape(1,16)
    loaded_model = pickle.load(open("model_logreg_best.pkl","rb"))
    result = loaded_model.predict(to_predict)
    return result[0]

@app.route('/result',methods = ['POST'])
def result():
    if request.method == 'POST':
        to_predict_list = request.form.to_dict()
        to_predict_list=list(to_predict_list.values())
        to_predict_list = list(map(float, to_predict_list))
        result = ValuePredictor(to_predict_list)
        if int(result)==1:
            prediction='Terdapat tanda dari Retinopati Diabetik'
        else:
            prediction='Tidak ada tanda terjadi Retinopati Diabetik'
    
    return render_template("result.html",prediction=prediction, result=result)

if __name__ == "__main__":
    app.debug=True
    app.run()