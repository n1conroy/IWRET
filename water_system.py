from flask import Flask, render_template, json, request
import numpy as np
import pysd
import os
import matplotlib
import json
import random
import csv
matplotlib.use('Agg')
import matplotlib.pyplot as plt
plt.ioff()
from threading import Lock
lock = Lock()
import datetime
import mpld3
from mpld3 import plugins

def draw_fig(data):
    with lock:
        fig, ax = plt.subplots()
        with open('water_demand.csv', 'wb') as f:  
            w = csv.DictWriter(f, data.keys())
            w.writeheader()
            w.writerow(data)
	model = pysd.read_vensim ('IWRET_7.mdl')
        # remove all checkbox elements
	for k,v in data.items():
            if v == 'on' or k=='undefined':
               del data[k]
        print data
        #####    conflict for vlad  ####
        del data['Unit Industrial Demand']

	modeldata = model.run(params=data, return_columns=['SF Stock of Units'])
        x = range(731)
	y = modeldata
        ax.plot(x, y)
    return mpld3.fig_to_html(ax)


templateDir = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'templates');
app = Flask (__name__, template_folder=templateDir);

@app.route('/')
def home():
    return render_template("index.html")


@app.route('/query', methods=['POST'])
def query():
   data = json.loads(request.data)
   return draw_fig(data)


if __name__ == '__main__':
    app.run(debug=True)
