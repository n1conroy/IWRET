#!/usr/bin/python

from flask import Flask
from flask import request
from flask import render_template
import sys
import numpy as np
import pandas as pd
import pysd
import matplotlib.pyplot as plt

app = Flask(__name__)
@app.route('/')

def water_system():
    return render_template("water_system.html")
@app.route('/', methods=['POST'])


def water_system_post():
    #text = request.form['SF Initial Stock of Units','MF Initial Stock of Units']
    model = pysd.read_vensim ('teacup.mdl') # Reads and converts MDL file into a Python Class
    x= model.run()
    values = model.run(params={'final_time':11.23,'heat_loss_to_room':67.98,'saveper':87.9,'time_step':2,'initial_time': 23.238},return_columns=['characteristic_time', 'room_temperature','teacup_temperature']) # Resulting Variables
    
    s = 1 + np.sin(2 * np.pi * values)
    fig, ax = plt.subplots()
    ax.plot(s, values)

    ax.set (xlabel='time (s)', ylabel='water usage (l/d)',
       title ='Water System')
    ax.grid
    #plt.show()
    return str(s) 

if __name__ == '__main__':
    app.run()
