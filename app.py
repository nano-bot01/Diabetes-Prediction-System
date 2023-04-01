# -*- coding: utf-8 -*-
"""
Created on Mon Mar 27 23:46:19 2023

@author: ankit
"""


import numpy as np
import pickle
import streamlit as st
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn import svm
from xgboost import XGBClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import confusion_matrix,  accuracy_score, classification_report
from sklearn.metrics import accuracy_score


# loading the saved model 
loaded_model = pickle.load(open("trained_model.sav",'rb'))

# temp = open("trained_model.pkl","rb")
# loaded_model=pickle.load(temp)

# creating a function for prediction 

def diabetes_prediction(input_data):
    
    
    # changing data to numpy array 
    input_data_array = np.asarray(input_data)
    
    # reshape the array as we are predicting for one instance
    input_data_reshaped =  input_data_array.reshape(1,-1)
    
    result = loaded_model.predict(input_data_reshaped)
    print("The prediction is : ",result)
    
    if (result[0] == 0):
      return "The person is not Diabetic"
    else:
      return "The person is Diabetic"
  

def main():
    # giving a title 
    #st.title('Diabetes Prediction Application')
    st.markdown("<h1 style='text-align: center; color: red;'>Diabetes Prediction Application</h1>", unsafe_allow_html=True)
    
    # getting the input data from input user
    
    Pregnancies = st.text_input("Number of Pregnancies : ")
    Glucose = st.text_input("Glucose level : ")
    BloodPressure = st.text_input("Blood Pressure value: ")
    SkinThickness = st.text_input("Measure of Skin Thickness : ")
    Insulin = st.text_input("Insulin level : ")
    BMI = st.text_input("BMI value : ")
    DiabetesPedigreeFunction = st.text_input("Diabetes Pedigree Function value : ")
    Age= st.text_input("Age of person : ")
    
    
    # code for prediction 
    diagnosis = '' # null string 
    
    # creating a button for prediction 
    
    if st.button('Diagonasis Test Result'):
        diagnosis = diabetes_prediction([Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin, BMI, DiabetesPedigreeFunction, Age ])
        
    st.success(diagnosis)
    
    st.markdown("***")
    
    st.markdown("""
    About the data to be filled : 
        
        Pregnancies: Number of times pregnant 
        Glucose: Plasma glucose concentration a 2 hours in an oral glucose tolerance test
        BloodPressure: Diastolic blood pressure (mm Hg)
        SkinThickness: Triceps skin fold thickness (mm)
        Insulin: 2-Hour serum insulin (mu U/ml)
        BMI: Body mass index (weight in kg/(height in m)^2)
        DiabetesPedigreeFunction: Diabetes pedigree function
        Age: Age (years)
        Outcome: Class variable (0 or 1)""")
    
    st.text("\n\n")
    st.markdown("<h3 style='text-align: center; color: red;'>Model accuracy is only 77% </h3>", unsafe_allow_html=True)
    
    
    st.write(" \n\n\n\n\n\n")
    st.markdown("******")
    
    st.write("Contributor : [Ankit Nainwal](https://github.com/nano-bot01)")
    
    
if __name__ == '__main__':
    main()
    
    
