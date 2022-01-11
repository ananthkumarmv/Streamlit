# -*- coding: utf-8 -*-
"""
Created on Tue Jan 11 07:21:10 2022

@author: Unbeknownstguy
"""

import streamlit as st


# There are several widgets available in streamlit, like st.selectbox, st.checkbox, st.slider, and etc. 
value = st.selectbox('val') # this is widget
st.write(value, 'squared is', value * value)
