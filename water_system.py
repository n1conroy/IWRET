#!/usr/bin/python

from flask import Flask, render_template, json, request
import numpy as np
import pysd
import os
import matplotlib
import json
import random

matplotlib.use('Agg')
import matplotlib.pyplot as plt
plt.ioff()

from threading import Lock
lock = Lock()
import datetime
import mpld3
from mpld3 import plugins



s = json.load(open("./static/bmh_EXmatplotlibrc.json"))

x = range(100)
y = [a * 2 + random.randint(-20, 20) for a in x]

model = pysd.read_vensim ('teacup.mdl')
#result = request.form
modeldata = model.run()

def draw_fig(fig_type):
    with lock:
        fig, ax = plt.subplots()
        if fig_type == "line":
            ax.plot(x, y)
        elif fig_type == "bar":
            ax.bar(x, y)
        elif fig_type == "pie":
            ax.pie(pie_fracs, labels=pie_labels)
        elif fig_type == "scatter":
            ax.scatter(x, y)
        elif fig_type == "hist":
            ax.hist(y, 10, normed=1)
        elif fig_type == "area":
            ax.plot(x, y)
            ax.fill_between(x, 0, y, alpha=0.2)


    return mpld3.fig_to_html(fig)


templateDir = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'templates');
app = Flask (__name__, template_folder=templateDir);

@app.route('/')
def home():
    #return render_template("water_system.html")
    return render_template("index.html")


@app.route('/query', methods=['POST'])
def query():
    data = json.loads(request.data)
    return draw_fig(data["plot_type"])

#def result():
#    return render_template('well.html')  


if __name__ == '__main__':
    app.run(debug=True)

