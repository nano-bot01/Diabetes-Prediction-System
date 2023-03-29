# -*- coding: utf-8 -*-
"""
Created on Tue Mar 28 10:28:19 2023

@author: ankit
"""

import json
import requests


url = 'http://dfa1-104-196-157-129.ngrok.io/diabetes_prediction'

input_data_for_model = {

    'Pregnancies' : 8,
    'Glucose' : 85,
    'BloodPressure' : 55,
    'SkinThickness' : 20,
    'Insulin' : 0,
    'BMI' : 24.4,
    'DiabetesPedigreeFunction' : 0.136,
    'Age' : 42
    
    }

input_json = json.dumps(input_data_for_model)

response = requests.post(url, data=input_json)

print(response.text)
