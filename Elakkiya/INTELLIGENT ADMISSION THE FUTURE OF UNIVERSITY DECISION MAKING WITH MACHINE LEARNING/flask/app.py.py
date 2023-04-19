import numpy as np
from flask import Flask, request, jsonify, render_template
import pickle
app=Flask(__name__)
#import necessary libraries
from tensorflow.keras.models import load_model
#model = pickel.load(open('university.pkl','rb'))
#load model trained model
#load your trained model
model=load_model('model.h5')
@app.route('/')
def home();
   return render_template("elakkiya.html")
@app.route('/y-predict',method=['POST'])
def y-predict();
   For rendering results on HTML GUI
   #min max scaling
   min 1=[290.0,92.0,1.0,1.0,1.0,6.8,0.0]
   max 1=[340.0,120.0,5.0,5.0,5.0,5.0,9.92,1.0]
   k=[float(x)for x in request.from.value()]
   p=[]
   for i in range(7)
       l=(k[i]-min 1[i])/(max[i]-min 1[i])
       p.append(1)
  prediction=model.predict([p])
  print(prediction)
  output=prediction[0]
  if(output==False):
      return render-render_template('no chance.html',prediction-text="you dont have a chance")
  else:
      return render-render_template('chance.html',prediction-text="you have a chance")
if-name-=="-main":
  app.run(debug=False)