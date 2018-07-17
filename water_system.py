#!/usr/bin/python

from flask import Flask, flash, redirect, render_template, request, session, abort
import os
import sys
import numpy as np
import pandas as pd
import json
import pysd
import urllib2
import gviz_api
from gviz_data_table import Table


templateDir = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'templates');
app = Flask (__name__, template_folder=templateDir);

@app.route('/')
def water_system():
    return render_template("water_system.html")

@app.route('/result', methods=['POST'])

def result():
    model = pysd.read_vensim ('teacup.mdl') 
    result = request.form
    params= {
	'final_time':11.23,
	'heat_loss_to_room':67.98,
	'saveper':23.2,
	'time_step':104.2,
	'initial_time': 12.34, 
 	'final_time':7.8	
      }  
    return_columns = [
	'characteristic_time', 
	'room_temperature',
	'teacup_temperature'
	]   
   
    data = model.run(params=params,return_columns=return_columns)
    table = Table()
    table.add_column('characteristic_time', int, 'CT')
    table.add_column('room_temperature', int, 'RT')
    table.add_column('teacup_temperature', int, 'TT')
    for row in data.iterrows():
        print row[1].tolist()
    	table.append(row[1].tolist())
   
    for key,value in table:
	print (key,value)
    return render_template('well.html', data=data)
    
'''
    description= {("characteristic_time"):[('value')]}
    data_table= gviz_api.DataTable(description)
    data_table.LoadData(table) 
    json= data_table.ToJSon()
'''
 #   return render_template('well.html', data=data)

if __name__ == '__main__':
    app.run(debug=True)

