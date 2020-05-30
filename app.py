import streamlit as st
import pandas as pd
import numpy as np

# st.title("Hello world!")
# st.markdown("## My first streamlit dashboard!")
# https://send.firefox.com/download/7c06286052eef380/#q8Sn_ka6TWOP8tN3MsdXOg

DATA_URL = (
 "/home/rhyme/Desktop/motorvechile-mlds/mvcrashes.csv"
)
st.title("Motor vehicle collision in new york city")
st.markdown("This application is a streamlit application to analyse motor vehicle collision in nyc")

@st.cache(persist=True)
def load_data(nrows):
    data = pd.read_csv(DATA_URL, nrows=nrows, parse_dates=[['CRASH_DATE', 'CRASH_TIME']])
    data.dropna(subset=['LATITUDE', 'LONGITUDE'], inplace=True)
    lowercase = lambda x: str(x).lower()
    data.rename(lowercase, axis='columns', inplace=True)
    data.rename(columns={'crash_date_crash_time': 'date/time'}, inplace=True)
    return data

data = load_data(100000)

if st.checkbox("Show raw data", False):
    st.subheader('Row data')
    st.write(data)
