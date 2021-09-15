import numpy as np
from flask import Flask, request, jsonify, render_template, abort
from flask_sqlalchemy import SQLAlchemy
import model
import os
from os.path import join, dirname, realpath
import pandas as pd


app = Flask(__name__)
app.config['SECRET_KEY'] = '5791628bb0b13ce0c676dfde280ba245'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# app.config["DEBUG"] = True


db = SQLAlchemy(app)

class Data(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    latitude = db.Column(db.Float, nullable=False)
    longitude = db.Column(db.Float, nullable=False)
    epoch = db.Column(db.Float, nullable=False)
    orientation = db.Column(db.Float, nullable=False)

    def to_json(self):

        return {
            "latitude": self.latitude,
            "longitude": self.longitude,
            "epoch": self.epoch,
            "orientation": self.orientation
        }


    def __repr__(self):
        return f"Data('{self.latitude}', '{self.longitude}', '{self.epoch}', '{self.orientation}')"



@app.route('/<latitude>/<longitude>/<epoch>/<orientation>', methods=['GET','POST'])
def index(latitude, longitude, epoch, orientation):


    data = Data(latitude=latitude, longitude=longitude, epoch=epoch, orientation=orientation)
    
    db.session.add (data)
    db.session.commit()
    a = data.to_json()
    b = model.is_glare_request(a)
    return b


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/predict',methods=['GET','POST'])
def predict():
    request_features = [x for x in request.form.values()]
    final_features = [np.array(request_features)]


    prediction = model.is_glare_ui(final_features)

    output = prediction

    return render_template('index.html', prediction_text='Does the image have glare? $ {}'.format(output))


@app.route('/results',methods=['GET','POST'])
def results():

    data = request.json(force=True)
    prediction = model.is_glare_ui([np.array(list(data.values()))])

    output = prediction
    return jsonify(output)

if __name__ == "__main__":
    app.run(debug=True)
