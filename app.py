from flask import Flask, render_template, request, redirect
import pickle
import sklearn
import numpy as np

app=Flask(__name__, template_folder='templates')

model = pickle.load(open('knn_pickle', 'rb'))

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/form_predict')
def form_predict():
    return render_template('artikel.html')

if __name__=="__main__":
    app.run(debug=True)