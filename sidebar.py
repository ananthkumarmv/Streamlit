# -*- coding: utf-8 -*-
"""
Created on Tue Jan 11 12:30:26 2022

@author: Unbeknownstguy
"""

import streamlit as st

st.title("Streamlit")

selectbox = st.sidebar.selectbox(
    "Select Yes or No", ["Yes", "No"]
)

st.write(f"You selected {selectbox}")
