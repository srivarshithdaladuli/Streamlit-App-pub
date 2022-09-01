import streamlit as st
import pandas as pd
import numpy as np

df = pd.read_csv('data/clean_open_pubs_data.csv')
st.title('Pubs Location on Authority Name')
title = st.text_input('Enter local authority name', 'Babergh')
st.markdown(title)

fetching_local_data = df.loc[df.local_authority == title,['latitude','longitude']]
st.map(fetching_local_data)

fetching_local_name = df.loc[df.local_authority == title,['name','address']].reset_index(drop=True)
st.markdown('Area Name"s and Address')
st.dataframe(fetching_local_name)