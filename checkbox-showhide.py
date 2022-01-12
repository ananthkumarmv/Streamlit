# -*- coding: utf-8 -*-
"""
Created on Wed Jan 12 17:58:29 2022

@author: Unbeknownstguy
"""

import streamlit as st

# checkbox
# check if the checkbox is checked
# title of the checkbox is 'Show/Hide'

if st.checkbox("Show/Hide"):
    
    # display the text if the checkbox returns True value
    st.text("Showing the widget")


