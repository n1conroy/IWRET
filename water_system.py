#!/usr/bin/python

from flask import Flask, flash, redirect, render_template, request, session, abort
import os
import sys
import numpy as np
import pandas as pd
import json
import pysd
import urllib2

templateDir = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'templates');
app = Flask (__name__, template_folder=templateDir);

@app.route('/')
def water_system():
    return render_template("water_system.html")

@app.route('/', methods=['POST'])

def well_data():
    #text = request.form['SF Initial Stock of Units','MF Initial Stock of Units']
    model = pysd.read_vensim ('teacup.mdl') 
    data = model.run(params={'final_time':11.23,'heat_loss_to_room':67.98,'saveper':87.9,'time_step':2,'initial_time': 23.238},return_columns=['characteristic_time', 'room_temperature','teacup_temperature'])
    print (data)
    return render_template('well.html', data=data)

if __name__ == '__main__':
    app.run()

