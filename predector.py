# -*- coding: utf-8 -*-
"""
Created on Mon Mar 27 23:31:32 2023

@author: ankit
"""


import numpy as np
import pandas as pd
import pickle
from flask import Flask, request, render_template


# loading the saved model 
loaded_model = pickle.load(open("trained_model.sav",'rb'))



input_data = (5,166,72,19,175,25.8,0.587,51)

# changing data to numpy array 
input_data_array = np.asarray(input_data)

# reshape the array as we are predicting for one instance
input_data_reshaped =  input_data_array.reshape(1,-1)

result = loaded_model.predict(input_data_reshaped)
print("The prediction is : ",result)

if (result[0] == 0):
  print("The person is not Diabetic")
else:
  print("The person is Diabetic")