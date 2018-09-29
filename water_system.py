from flask import Flask, render_template, json, request
import numpy as np
import pysd
import pandas as pd
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
templateDir = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'templates');

app = Flask (__name__, template_folder=templateDir);

def draw_figs(data):
    with lock:
        fig, ax = plt.subplots()
        fig=plt.figure(figsize=(2,2))


        output_fields = ['SF Stock of Units','MF Stock of Units',
                         'SF Units Total Area Occupied', 'SF Total Area for Irrigation',
                         'SF Rate of Adoption', 'MF Rate of Adoption', 'SF Average Occupancy per Unit',
                         'MF Average Occupancy per Unit','Domestic Demand','Irrigation Demand',
                         'Commercial and Institutional Demand','Daily Water Demand','Result Reached System Capacity']
        with open('water_demand.csv', 'wb') as f:  
            w = csv.DictWriter(f, data.keys())
            w.writeheader()
            w.writerow(data)
	model = pysd.read_vensim ('IWRET_10.mdl')
        # remove all checkbox elements
	for k,v in data.items():
            if v == 'on' or k=='undefined':
               del data[k]

	modeldata = model.run(params=data,return_columns=output_fields)
        dict_of_plots=list()

        x1 = range(731)
	y1 = modeldata[output_fields[0]]
        indata=pd.DataFrame(x1,y1)
        indata.plot(ax=ax)
        single_chart=dict()
        single_chart['id']="graph_container1"
        single_chart['json']=json.dumps(mpld3.fig_to_dict(fig))
        dict_of_plots.append(single_chart)

      
        x2 = range(731)
	y2 = modeldata[output_fields[1]]
        indata=pd.DataFrame(x2,y2)
        indata.plot(ax=ax)
        single_chart=dict()
        single_chart['id']="graph_container2"
        single_chart['json']=json.dumps(mpld3.fig_to_dict(fig))
        dict_of_plots.append(single_chart)

        x3 = range(731)
	y3 = modeldata[output_fields[2]]
        indata=pd.DataFrame(x3,y3,)
        indata.plot(ax=ax)
        single_chart=dict()
        single_chart['id']="graph_container3"
        single_chart['json']=json.dumps(mpld3.fig_to_dict(fig))
        dict_of_plots.append(single_chart)       
       

        x4 = range(731)
	y4 = modeldata[output_fields[3]]
        indata=pd.DataFrame(x4,y4,)
        indata.plot(ax=ax)
        single_chart=dict()
        single_chart['id']="graph_container4"
        single_chart['json']=json.dumps(mpld3.fig_to_dict(fig))
        dict_of_plots.append(single_chart)

        x5 = range(731)
	y5 = modeldata[output_fields[4]]
        indata=pd.DataFrame(x5,y5,)
        indata.plot(ax=ax)
        single_chart=dict()
        single_chart['id']="graph_container5"
        single_chart['json']=json.dumps(mpld3.fig_to_dict(fig))
        dict_of_plots.append(single_chart)

        x6 = range(731)
	y6 = modeldata[output_fields[5]]
        indata=pd.DataFrame(x6,y6,)
        indata.plot(ax=ax)
        single_chart=dict()
        single_chart['id']="graph_container6"
        single_chart['json']=json.dumps(mpld3.fig_to_dict(fig))
        dict_of_plots.append(single_chart)
        


       
        return render_template("results.html", dict_of_plots=dict_of_plots)#snippet=plot_snippet)
'''
        x4 = range(731)
        y4 = modeldata[output_fields[3]]
        ax4.plot(x4, y4)

        x5 = range(731)
        y5 = modeldata[output_fields[4]]
        ax5.plot(x5, y5)

        x6 = range(731)
        y6 = modeldata[output_fields[5]]
        ax6.plot(x6, y6)

    params[2]=mpd3.fig_to_html(fig3)
    params[3]=mpd3.fig_to_html(fig4)
    params[4]=mpd3.fig_to_html(fig5)
    params[5]=mpd3.fig_to_html(fig6)
'''


@app.route('/')
def home():

    
    return render_template("index.html")


@app.route('/query', methods=['POST'])
def query():
   data = json.loads(request.data)
   return draw_figs(data)


if __name__ == '__main__':
    app.run(debug=True)
