# -*- coding: utf-8 -*-
"""
Created on Tue Jan 11 12:03:55 2022

@author: Unbeknownstguy
"""

import numpy as np
import pandas as pd
import streamlit as st


st.title("Streamlit!")

st.write("Line Chart in Streamlit")
# 10 * 2 dimensional data

chart_data = pd.DataFrame(
    np.random.randn(10, 2),
    columns = [f"Col{i+1}" for i in range(2)])


st.line_chart(chart_data)
