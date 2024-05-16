import streamlit as st
import pandas as pd
import numpy as np

if st.checkbox('Show dataframe'):
    chart_data = pd.DataFrame(
       np.random.randint(0,50, size=(10,3)), columns=['FP101', 'FP201', 'FP301'])
    chart_data.index=['2014','2015','2016','2017','2018','2019','2020','2021','2022','2023']
    chart_data
