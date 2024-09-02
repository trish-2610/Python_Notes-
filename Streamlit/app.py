import streamlit as st 
import numpy as np 
import pandas as pd

## Title of the application
st.title("Hello Trishansh")

## write a simple text 
st.write("Streamlit is crazy")
st.write("Streamlit is amazing")

## Create a dataframe 
df = pd.DataFrame({
    "A" : [1,2,3,4],
    "B" : [5,6,7,8]
})

st.write("This is a DataFrame")
st.write(df)

## Creating a line chart 
chart_data = pd.DataFrame(
    np.random.randn(20,3) , columns = ["a","b","c"]
)

st.line_chart(chart_data)