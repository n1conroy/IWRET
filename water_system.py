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


def ReuseRecycledrawfigs(data):
        fig, ax = plt.subplots()
        with open('neighhydro.csv', 'wb') as f:  
            w = csv.DictWriter(f, data.keys())
            w.writeheader()
            w.writerow(data)
        print data
	model = pysd.read_vensim ('IWRET_13.mdl')
        for k,v in data.items():
            if v == 'on' or k=='undefined' or k=='formId':
               del data[k]
        modeldata=model.run(params=data, return_columns=['RH Total Water Harvested'])
        glist = ['RH Total Water Harvested','IA Runoff Daily','IA Runoff Total',
             'GWS Tank Inflow','Water Reuse Daily','Result RR LCC',
             'Result RR GHG Emissions','Result RR Energy']
        dict_of_plots=list()
        x1 = range(7301)
	y1 = modeldata['LU Sum']
        indata=pd.DataFrame(x1,y1)
        indata.plot(ax=ax)
        single_chart=dict()
        single_chart['id']="NeighHyd1"
        single_chart['json']=json.dumps(mpld3.fig_to_dict(fig))
        dict_of_plots.append(single_chart)    
        return render_template("results.html", dict_of_plots=dict_of_plots)#snippet=plot_snippet)



def NeighborhoodHyddraw_figs(data):
    with lock:
        fig, ax = plt.subplots()
        with open('neighhydro.csv', 'wb') as f:  
            w = csv.DictWriter(f, data.keys())
            w.writeheader()
            w.writerow(data)
	model = pysd.read_vensim ('IWRET_13.mdl')
        for k,v in data.items():
            if v == 'on' or k=='undefined' or k=='formId':
               del data[k]
        modeldata=model.run(params=data, return_columns=['SW Daily Rate'])
        glist =['LU Sum','CN Composite','Rainfall','SW Daily Rate']
        dict_of_plots=list()
        x1 = range(7301)
	y1 = modeldata['CN Composite']
        indata=pd.DataFrame(x1,y1)
        indata.plot(ax=ax)
        single_chart=dict()
        single_chart['id']="NeighHyd1"
        single_chart['json']=json.dumps(mpld3.fig_to_dict(fig))
        dict_of_plots.append(single_chart)      

        return render_template("results.html", dict_of_plots=dict_of_plots)#snippet=plot_snippet)
    


def Pumpingdraw_figs(data):
    with lock:
        fig, ax = plt.subplots()
        with open('pumping.csv', 'wb') as f:  
            w = csv.DictWriter(f, data.keys())
            w.writeheader()
            w.writerow(data)
	model = pysd.read_vensim ('IWRET_13.mdl')
        for k,v in data.items():
            if v == 'on' or k=='undefined' or k=='formId':
               del data[k]
        modeldata=model.run(params=data, return_columns=['Result Pumping LCC'])
        glist =['Result Pumping LCC', 'Result Pumping GHG Emissions', 'Result Pumping Energy']

        dict_of_plots=list()
        x1 = range(7301)
	y1 = modeldata['Result Pumping LCC']
        indata=pd.DataFrame(x1,y1)
        indata.plot(ax=ax)
        single_chart=dict()
        single_chart['id']="Pumping1"
        single_chart['json']=json.dumps(mpld3.fig_to_dict(fig))
        dict_of_plots.append(single_chart)      

        '''
        x2 = range(7301)
	y2 = modeldata['Result Pumping GHG Emissions']
        indata=pd.DataFrame(x2,y2)
        indata.plot(ax=ax)
        single_chart=dict()
        single_chart['id']="WD2"
        single_chart['json']=json.dumps(mpld3.fig_to_dict(fig))
        dict_of_plots.append(single_chart)
        
        x3 = range(7301)
	y3 = modeldata['Result Pumping Energy']
        indata=pd.DataFrame(x3,y3,)
        indata.plot(ax=ax)
        single_chart=dict()
        single_chart['id']="WD3"
        single_chart['json']=json.dumps(mpld3.fig_to_dict(fig))
        dict_of_plots.append(single_chart)

        '''
        return render_template("results.html", dict_of_plots=dict_of_plots)#snippet=plot_snippet)
    
def WDdraw_figs(data):
    with lock:
        fig, ax = plt.subplots(2, 2, figsize=(3, 2),sharex='col', sharey='row')
        fig.subplots_adjust(hspace=0.1, wspace=0.1)
        for key in sorted(data):
             print "%s: %s" % (key, data[key])
        with open('water_demand.csv', 'wb') as f:  
            w = csv.DictWriter(f, data.keys())
            w.writeheader()
            w.writerow(data)
	model = pysd.read_vensim ('IWRET_17_DWD.mdl')
        # remove all checkbox elements
	for k,v in data.items():
            if v == 'on' or k=='undefined' or k=='formId':
               del data[k]
        modeldata=model.run(params=data,return_columns=['MF Rate of Adoption', 'Result Reached System Capacity'])
        #modeldata=model.run(params=data)

        #modeldata=model.run(params=data, return_columns=[ 'MF Rate of Adoption', 'Result Reached System Capacity','MF Stock of Units','SF Stock of Units','SF Rate of Adoption','SF Average Occupancy per Unit'])
        dict_of_plots=list()
        x1 = range(731)
	y1 = modeldata['MF Rate of Adoption']
        indata=pd.DataFrame(x1,y1)
        indata.plot(ax=ax)
        single_chart=dict()
        single_chart['id']="WD1"
        single_chart['json']=json.dumps(mpld3.fig_to_dict(fig))
        dict_of_plots.append(single_chart)      
        '''
        x2 = range(7301)
	y2 = modeldata['Result Reached System Capacity']
        indata=pd.DataFrame(x2,y2)
        indata.plot(ax=ax)
        single_chart=dict()
        single_chart['id']="WD2"
        single_chart['json']=json.dumps(mpld3.fig_to_dict(fig))
        dict_of_plots.append(single_chart)
        
        x3 = range(7301)
	y3 = modeldata['MF Stock of Units']
        indata=pd.DataFrame(x3,y3,)
        indata.plot(ax=ax)
        single_chart=dict()
        single_chart['id']="WD3"
        single_chart['json']=json.dumps(mpld3.fig_to_dict(fig))
        dict_of_plots.append(single_chart)       
        
        x4 = range(7301)
	y4 = modeldata['SF Stock of Units']
        indata=pd.DataFrame(x4,y4,)
        indata.plot(ax=ax)
        single_chart=dict()
        single_chart['id']="WD4"
        single_chart['json']=json.dumps(mpld3.fig_to_dict(fig))
        dict_of_plots.append(single_chart)
        
        x5 = range(7301)
	y5 = modeldata['SF Units Total Area Occupied']
        indata=pd.DataFrame(x5,y5,)
        indata.plot(ax=ax)
        single_chart=dict()
        single_chart['id']="WD5"
        single_chart['json']=json.dumps(mpld3.fig_to_dict(fig))
        dict_of_plots.append(single_chart)
        
        x6 = range(7301)
	y6 = modeldata['SF Total Area for Irrigation']
        indata=pd.DataFrame(x6,y6,)
        indata.plot(ax=ax)
        single_chart=dict()
        single_chart['id']="WD6"
        single_chart['json']=json.dumps(mpld3.fig_to_dict(fig))
        dict_of_plots.append(single_chart)
        
        x7 = range(7301)
	y7 = modeldata['SF Rate of Adoption']
        indata=pd.DataFrame(x7,y7,)
        indata.plot(ax=ax)
        single_chart=dict()
        single_chart['id']="WD7"
        single_chart['json']=json.dumps(mpld3.fig_to_dict(fig))
        dict_of_plots.append(single_chart)
        
        x8 = range(7301)
	y8 = modeldata['SF Average Occupancy per Unit']
        indata=pd.DataFrame(x8,y8,)
        indata.plot(ax=ax)
        single_chart=dict()
        single_chart['id']="WD8"
        single_chart['json']=json.dumps(mpld3.fig_to_dict(fig))
        dict_of_plots.append(single_chart)

        x9 = range(7301)
	y9 = modeldata['MF Average Occupancy per Unit']
        indata=pd.DataFrame(x9,y9,)
        indata.plot(ax=ax)
        single_chart=dict()
        single_chart['id']="WD9"
        single_chart['json']=json.dumps(mpld3.fig_to_dict(fig))
        dict_of_plots.append(single_chart)
        
        x10 = range(7301)
	y10 = modeldata['Domestic Demand']
        indata=pd.DataFrame(x10,y10,)
        indata.plot(ax=ax)
        single_chart=dict()
        single_chart['id']="WD10"
        single_chart['json']=json.dumps(mpld3.fig_to_dict(fig))
        dict_of_plots.append(single_chart)
        

        x11 = range(7301)
	y11 = modeldata['Irrigation Demand']
        indata=pd.DataFrame(x11,y11,)
        indata.plot(ax=ax)
        single_chart=dict()
        single_chart['id']="WD11"
        single_chart['json']=json.dumps(mpld3.fig_to_dict(fig))
        dict_of_plots.append(single_chart)
        
        x12 = range(7301)
	y12 = modeldata['Commercial and Institutional Demand']
        indata=pd.DataFrame(x12,y12,)
        indata.plot(ax=ax)
        single_chart=dict()
        single_chart['id']="WD12"
        single_chart['json']=json.dumps(mpld3.fig_to_dict(fig))
        dict_of_plots.append(single_chart)
        

        x13 = range(7301)
	y13 = modeldata['Daily Water Demand']
        indata=pd.DataFrame(x13,y13,)
        indata.plot(ax=ax)
        single_chart=dict()
        single_chart['id']="WD13"
        single_chart['json']=json.dumps(mpld3.fig_to_dict(fig))
        dict_of_plots.append(single_chart)
        
        x14 = range(7301)
	y14 = modeldata['Years']
        indata=pd.DataFrame(x14,y14,)
        indata.plot(ax=ax)
        single_chart=dict()
        single_chart['id']="WD14"
        single_chart['json']=json.dumps(mpld3.fig_to_dict(fig))
        dict_of_plots.append(single_chart)
        '''
        return render_template("results.html", dict_of_plots=dict_of_plots)#snippet=plot_snippet)



@app.route('/')
def home():    
    return render_template("index.html")


@app.route('/query', methods=['POST'])
def query():
   d = json.loads(request.data)
   data= ast.literal_eval(json.dumps(d))
   '''for key in sorted(data):
      print "%s: %s" % (key, data[key])
   '''
   return WDdraw_figs(data)   

   '''
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
        return Pumpingdraw_figs(data)
   elif data['formId']=='NeighborhoodHydrology':
        return NeighborhoodHyddraw_figs(data)
   elif data['formId']=='ReuseRecycleSystems':
        return WDdraw_figs(data)
   '''
if __name__ == '__main__':
    app.run(debug=True)
