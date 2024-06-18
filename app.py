import os
import numpy as np
import pickle
import streamlit as st
import warnings 
#Set Page Configuuration
st.set_page_config(page_title="Health Assistant",
                   layout="wide",
                   page_icon="👩🏻‍⚕️")

#getting the working directory of the main.py
working_dir=os.path.dirname(os.path.abspath(__file__))

#loading the saved models
heart_disease_model=pickle.load(open('C:/Users/ELCOT/Documents/Data Science/Projects/Heart Disease Prediction using SVM/heart_disease_model.sav','rb'))




#Heart Disease Prediction
st.title('Heart Disease Prediction using ML')
col1,col2,col3=st.columns(3)

with col1:
    age=st.text_input('Age')

with col2:
    sex=st.text_input('Sex (Male:1 | Female:0)')
   

with col3:
    cp=st.text_input('Chest Pain (Angina:1|Carditis:2|Myocarditis:3|Cardiomyopathy:4)')

with col1:
    trestbps=st.text_input('Resting Blood Pressure')

with col2:
    chol=st.text_input('Serum Cholestral in mg/dl')

with col3:
    fbs=st.text_input('Fasting Blood Sugar > 120 mg/dl (Yes:1 | No:0)')

with col1:
    restecg=st.text_input('ECG results ( 0<ECG<60 : 0 | 60<ECG<120 : 1 | 120<ECG : 2)')

with col2:
    thalach=st.text_input('Maximum Heart Rate Achieved ')

with col3:
    exang=st.text_input('Exercise Induced Angina (Yes:1 | No:0)')

with col1:
    oldpeak=st.text_input('ST depression induced by exercise (0.0 < x < 4.0)')

with col2:
    slope=st.text_input('Slope of peak exercise (Upsloping:1| Flat:2| Downsloping:3)')

with col3:
    ca=st.text_input('Major vessels colored by flouroscopy ( 0 to 3)')

with col1:
    thal=st.text_input('Thallium (Normal:0| FixedDefect:1| ReversableDefect:2)')

#code for prediction
heart_diagnosis = ''

#creating a button for prediction
if st.button('Heart Disease Test Result'):
    user_input = [age,sex,cp,trestbps,chol,fbs,restecg,thalach,exang,oldpeak,slope,ca,thal]
    user_input = [float(x) for x in user_input]
    heart_prediction = heart_disease_model.predict([user_input])

    if heart_prediction[0] == 1:
        heart_diagnosis = 'The person is having heart disease'
    else:
        heart_diagnosis = 'The person does not have any heart disease'
st.success(heart_diagnosis)