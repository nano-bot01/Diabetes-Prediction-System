# -*- coding: utf-8 -*-
"""
Created on Mon Mar 27 23:46:19 2023

@author: ankit
"""


import numpy as np
import pickle
import streamlit as st

# loading the saved model 
# loaded_model = pickle.load(open("trained_model.pkl",'rb'))
loaded_model = pickle.load(open("model/trained_model.pkl",'rb'))

# creating a function for prediction 

def diabetes_prediction(input_data):
    
    
    # changing data to numpy array 
    input_data_array = np.asarray(input_data)
    
    # reshape the array as we are predicting for one instance
    input_data_reshaped =  input_data_array.reshape(1,-1)
    
    result = loaded_model.predict(input_data_reshaped)
    print("The prediction is : ",result)
    
    if (result[0] == 1):
      return "The person is Diabetic"        
    else:
      return "The person is not Diabetic"
  

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
    
    Sample data to fill: 
    
        4  110  92  32  88  31  0.248  26  => Non-Diabetic Person""")
    
    st.markdown("""
    
    About the data to be filled : 
        
        Pregnancies: Number of times pregnancy occurred (0, 0+)
        Glucose: Plasma glucose concentration a 2 hours in an oral glucose tolerance test (0 - 300)
        BloodPressure: Diastolic blood pressure (mm Hg) (0, 200)
        SkinThickness: Triceps skin fold thickness (mm) (0, 0+)
        Insulin: 2-Hour serum insulin (mu U/ml) 
        BMI: Body mass index (weight in kg/(height in m)^2) (9 - 72)
        DiabetesPedigreeFunction: Diabetes pedigree function (0.0 - 3.0)
        Age: Age (years) (0, 0+)
        Outcome: Class variable (0 or 1)""")
    
    st.text("\n\n")
#     st.markdown("<h3 style='text-align: center; color: red;'> Model accuracy is   </h3>", unsafe_allow_html=True)    
    
    st.write(" \n\n\n\n")
    st.markdown("******")
    
    st.write("Contributor : [Ankit Nainwal](https://github.com/nano-bot01) \n [LinkedIn](https://www.linkedin.com/in/ankit-nainwal1/)")
    
    st.write("\n© 2023 Diabetes Prediction System. All rights reserved.")
if __name__ == '__main__':
    main()
    
    
