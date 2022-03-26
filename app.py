import streamlit as st
import pandas as pd
from sklearn.linear_model import LinearRegression

st.header('Heart Disease Prediction')

dataset=pd.read_csv('heart.csv')

X=dataset.iloc[:,:-1].values
Y=dataset.iloc[:,-1].values
classifier=LinearRegression()
classifier.fit(X,Y)


a=st.text_input('Enter Age')
s=st.text_input('Enter Sex')
cp=st.text_input('Enter Cp')
t=st.text_input('Enter Trestbps')
c=st.text_input('Enter Cholestrol')
f=st.text_input('Enter Fbs')
r=st.text_input('Enter Restecg')
th=st.text_input('Enter Thalach')
e=st.text_input('Enter Exang')
o=st.text_input('Enter Oldpak')
sl=st.text_input('Enter Slope')
c=st.text_input('Enter Ca')
t=st.text_input('Enter Thal')



if st.button('Predict Heart Disease'):
    out=classifier.predict([[a,s,cp,t,c,f,r,th,e,o,sl,c,t]])[0]
    if(out==0):
        st.success('No Heart Disease')
    else:
        st.warning('Heart Disease Found')
        

            