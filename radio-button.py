# -*- coding: utf-8 -*-
"""
Created on Wed Jan 12 18:03:21 2022

@author: Unbeknownstguy
"""

import streamlit as st


# radio button
# first argument is the title of the radio button
# second argument is the options for the ratio button

status = st.radio("Select Gender: ", ('Male', 'Female'))


# conditional statement to print
# Male if male is selected else print female
# showing the result using the success function

if (status == 'Male'):
    st.success("Male")
else:
    st.success("Female")
    
    