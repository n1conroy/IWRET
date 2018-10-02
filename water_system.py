from flask import Flask, render_template, json, request
import numpy as np
import pysd
import pandas as pd
import os
import matplotlib
import json, ast
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

def Pumpingdraw_figs(data):
    with lock:
        fig, ax = plt.subplots()
        Pumpingoutput_fields = ['Years','SF Stock of Units','MF Stock of Units',
                         'SF Units Total Area Occupied', 'SF Total Area for Irrigation',
                         'SF Rate of Adoption', 'MF Rate of Adoption', 'SF Average Occupancy per Unit',
                         'MF Average Occupancy per Unit','Domestic Demand','Irrigation Demand',
                         'Commercial and Institutional Demand','Daily Water Demand','Result Reached System Capacity']
        with open('water_demand.csv', 'wb') as f:  
            w = csv.DictWriter(f, data.keys())
            w.writeheader()
            w.writerow(data)
	model = pysd.read_vensim ('IWRET_13.mdl')
        # remove all checkbox elements
	for k,v in data.items():
            if v == 'on' or k=='undefined' or k=='formId':
               del data[k]
	modeldata = model.run(params=data,return_columns=WDoutput_fields)
        dict_of_plots=list()
        x1 = range(1)
	y1 = modeldata[WDoutput_fields[0]]
        indata=pd.DataFrame(x1,y1)
        indata.plot(ax=ax)
        single_chart=dict()
        single_chart['id']="WD0"
        #single_chart['json']=json.dumps(mpld3.fig_to_dict(fig))
        single_chart['json']=y1
        dict_of_plots.append(single_chart)      
        return(dict_of_plots)
    
def WDdraw_figs(data):
    with lock:
        fig, ax = plt.subplots()
        WDoutput_fields = ['SF Stock of Units','MF Stock of Units',
                         'SF Units Total Area Occupied', 'SF Total Area for Irrigation',
                         'SF Rate of Adoption', 'MF Rate of Adoption', 'SF Average Occupancy per Unit',
                         'MF Average Occupancy per Unit','Domestic Demand','Irrigation Demand',
                         'Commercial and Institutional Demand','Daily Water Demand','Result Reached System Capacity']
        with open('water_demand.csv', 'wb') as f:  
            w = csv.DictWriter(f, data.keys())
            w.writeheader()
            w.writerow(data)
	model = pysd.read_vensim ('IWRET_13.mdl')
        # remove all checkbox elements
	for k,v in data.items():
            if v == 'on' or k=='undefined' or k=='formId':
               del data[k]
	#modeldata = model.run(params=data,return_columns=WDoutput_fields)
        modeldata=model.run(return_columns=WDoutput_fields)
        dict_of_plots=list()
        x1 = range(7301)
	y1 = modeldata[WDoutput_fields[0]]
        indata=pd.DataFrame(x1,y1)
        indata.plot(ax=ax)
        single_chart=dict()
        single_chart['id']="WD0"
        single_chart['json']=json.dumps(mpld3.fig_to_dict(fig))
        dict_of_plots.append(single_chart)      

        x2 = range(731)
	y2 = modeldata[WDoutput_fields[1]]
        indata=pd.DataFrame(x2,y2)
        indata.plot(ax=ax)
        single_chart=dict()
        single_chart['id']="WD1"
        single_chart['json']=json.dumps(mpld3.fig_to_dict(fig))
        dict_of_plots.append(single_chart)

        x3 = range(731)
	y3 = modeldata[WDoutput_fields[2]]
        indata=pd.DataFrame(x3,y3,)
        indata.plot(ax=ax)
        single_chart=dict()
        single_chart['id']="WD2"
        single_chart['json']=json.dumps(mpld3.fig_to_dict(fig))
        dict_of_plots.append(single_chart)       
       
        x4 = range(731)
	y4 = modeldata[WDoutput_fields[3]]
        indata=pd.DataFrame(x4,y4,)
        indata.plot(ax=ax)
        single_chart=dict()
        single_chart['id']="graph_container4"
        single_chart['json']=json.dumps(mpld3.fig_to_dict(fig))
        dict_of_plots.append(single_chart)

        x5 = range(731)
	y5 = modeldata[WDoutput_fields[4]]
        indata=pd.DataFrame(x5,y5,)
        indata.plot(ax=ax)
        single_chart=dict()
        single_chart['id']="graph_container5"
        single_chart['json']=json.dumps(mpld3.fig_to_dict(fig))
        dict_of_plots.append(single_chart)

        x6 = range(731)
	y6 = modeldata[WDoutput_fields[5]]
        indata=pd.DataFrame(x6,y6,)
        indata.plot(ax=ax)
        single_chart=dict()
        single_chart['id']="graph_container6"
        single_chart['json']=json.dumps(mpld3.fig_to_dict(fig))
        dict_of_plots.append(single_chart)
        return render_template("results.html", dict_of_plots=dict_of_plots)#snippet=plot_snippet)



@app.route('/')
def home():    
    return render_template("index.html")


@app.route('/query', methods=['POST'])
def query():
   d = json.loads(request.data)
   
   data= ast.literal_eval(json.dumps(d))
   
   if data['formId']=='WaterDemand':
        return WDdraw_figs(data)
   elif data['formId']=='NeighborhoodProperties':
        return WDdraw_figs(data)
   elif data['formId']=='WaterDistributionNetwork':
        return WDdraw_figs(data)
   elif data['formId']=='WaterTreatmentWorks':
        return WDdraw_figs(data)
   elif data['formId']=='SewerCollectionNetwork':
        return WDdraw_figs(data)
   elif data['formId']=='WastewaterTreatmentWorks':
        return WDdraw_figs(data)
   elif data['formId']=='PumpingStations':
        return WDdraw_figs(data)
   elif data['formId']=='NeighborhoodHydrology':
        return WDdraw_figs(data)
   elif data['formId']=='ReuseRecycleSystems':
        return WDdraw_figs(data)
if __name__ == '__main__':
    app.run(debug=True)
