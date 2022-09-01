import streamlit as st
st.balloons()
import pandas as pd
import numpy as np
    

st.header('Open Pub Data')
df = pd.read_csv('data/clean_open_pubs_data.csv')
st.dataframe(df)

st.header('Shape of Data')
st.dataframe(df.shape)
st.text('There is 50,563 active pubs in United Kingdom')