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



def draw_fig(plot_type):
    with lock:
        fig, ax = plt.subplots()
        ax.plot(x, y)
    return mpld3.fig_to_html(fig)


templateDir = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'templates');
app = Flask (__name__, template_folder=templateDir);

@app.route('/')
def home():
    return render_template("index.html")


@app.route('/query', methods=['POST'])
def query():
   data = json.loads(request.data)
   model = pysd.read_vensim ('IWRET_6.mdl')
   modeldata = model.run(params=data)
   x = range(731)
   y = modeldata
   return draw_fig(data)


if __name__ == '__main__':
    app.run(debug=True)
