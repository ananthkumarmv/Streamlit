# -*- coding: utf-8 -*-
"""
Created on Tue Jan 11 07:30:29 2022

@author: Unbeknownstguy
"""

import streamlit as st

st.title("Streamlit!")

selectbox = st.selectbox(
        "Select Yes or No",
        ["Yes", "No"]
)

st.write(f"You selected {selectbox}")
