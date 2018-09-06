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

model = pysd.read_vensim ('teacup.mdl')
modeldata = model.run()
x = range(241)
y = modeldata['Heat Loss to Room']


def draw_fig(fig_type):
    with lock:
        fig, ax = plt.subplots()
        if fig_type == "line":
            ax.plot(x, y)
        elif fig_type == "bar":
            ax.bar(x, y)
        elif fig_type == "hist":
            ax.hist(y, 10, normed=1)
    return mpld3.fig_to_html(fig)


templateDir = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'templates');
app = Flask (__name__, template_folder=templateDir);

@app.route('/')
def home():
    print( request.form)
    return render_template("layout.html")


@app.route('/query', methods=['POST'])
def query():
    data = json.loads(request.data)
    #return (data)
    return draw_fig(data["plot_type"])


if __name__ == '__main__':
    app.run(debug=True)

