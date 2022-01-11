# -*- coding: utf-8 -*-
"""
Created on Tue Jan 11 07:25:56 2022

@author: Unbeknownstguy
"""

import pandas as pd
import streamlit as st

st.title("Streamlit!")

st.write("Our first DAtaFrame")

st.write(
    pd.DataFrame({
        'A': [1,2,3,4],
        'B': [5,6,7,8]
        })
)