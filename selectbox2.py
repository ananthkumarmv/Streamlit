# -*- coding: utf-8 -*-
"""
Created on Wed Jan 12 18:08:17 2022

@author: Unbeknownstguy
"""

import streamlit as st


# Selection box
 
# first argument takes the titleof the selectionbox
# second argument takes options

hobby = st.selectbox("Hobbies: ", ['Dancing', 'Reading', 'Sports'])


# print the selected hobby
st.write("Your hobby is: ", hobby)

