# -*- coding: utf-8 -*-
"""
Created on Sat Jan 15 20:58:40 2022

@author: Unbeknownstguy
"""

import streamlit as st
import pandas as pd
import numpy as np


st.write('Map data')
data_of_map = pd.DataFrame(
  np.random.randn(1000, 2) / [60, 60] + [36.66, -121.6],
  columns = ['latitude', 'longitude'])
st.map(data_of_map)