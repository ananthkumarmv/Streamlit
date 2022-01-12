# -*- coding: utf-8 -*-
"""
Created on Wed Jan 12 18:23:13 2022

@author: Unbeknownstguy
"""

import streamlit as st

# st.button() returns a boolean value. It returns a True value when clicked else returns False.

# Creating a simple button that does nothing
st.button("Click here")


# Creating a button, that when clicked, shows a text

if(st.button("About")):
    st.text("Wink Wink ;)");



