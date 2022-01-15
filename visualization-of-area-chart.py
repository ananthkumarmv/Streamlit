# -*- coding: utf-8 -*-
"""
Created on Sat Jan 15 20:55:26 2022

@author: Unbeknownstguy
"""

import streamlit as st
import pandas as pd
import numpy as np

dataframe = pd.DataFrame(np.random.randn(10, 5),
  columns = ('col %d' % i
    for i in range(5)))
dataframe

st.write('This is a area_chart.')
st.area_chart(dataframe)

