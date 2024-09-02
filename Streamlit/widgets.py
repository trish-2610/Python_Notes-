import streamlit as st 
import pandas as pd

st.title("Stream Text Input")

## Input text box 
name = st.text_input("Enter your name")

if name : 
    st.write(f"Hello  {name}")

department = st.text_input("enter your department")

if department : 
    st.write(f"Department = {department}")

## Slider 
age = st.slider("Choose your age : " , 0 , 100 , 25) ## (starting value , end value , initial value)
st.write(f"AGE = {age}")

sl = st.slider("Trishansh ka level :" , 98, 100 ,99)

## selectbox
language = ["C++" , "Java" , "Python" , "Javasrcipt"]
sbox = st.selectbox("Choose your favorite programming language " , language)
st.write("Your favorite programming language is " , sbox)

## creating an uploader 
upload_data = st.file_uploader("Choose a CSV file",type="csv")
if upload_data is not None :
    df = pd.read_csv(upload_data)
    st.write(df)
