import numpy as np
import pandas as pd
import streamlit as st
import seaborn as sns
from pandas_profiling import ProfileReport
from streamlit_pandas_profiling import st_profile_report
import sys


# to shouw the title on webapp
st.markdown(''' 
 # **Exploratory Data Analysis web application**
 This app is developed by vedcode called as **EDA app**''')

#how to upload a file from pc

with st.sidebar.header("Upload your dataset (.csv)"):
    uploaded_file = st.sidebar.file_uploader("Upload your file", type=['csv'])
    df=sns.load_dataset('titanic')
    st.sidebar.markdown("[Example CSV file](https://github.com/Opensourcefordatascience/Data-sets/blob/master/blood_pressure.csv)")

# profiling report for pandas

if uploaded_file is not None:
    st.cache_data
    def load_csv():
        csv=pd.read_csv(uploaded_file)
        return csv

    df = load_csv()
    pr = ProfileReport(df,explorative=True)
    st.header('**Input DF**')
    st.write(df)
    st.write("---")
    st.header("**Profiling repot with pandas**")
    st_profile_report(pr)

else:
    st.info('Awaiting for CSV file')
    if st.button('Press the use example data'):
        st.cache_data
        def load_data():
            a=pd.DataFrame(np.random.rand(100,5),
                           columns=['patient','sex','agegrp','bp_before',	'bp_after'])
            return a
        df = load_data()
        pr = ProfileReport(df,explorative=True)
        st.header('**Input DF**')
        st.write(df)
        st.write("---")
        st.header("**Profiling repot with pandas**")
        st_profile_report(pr)

