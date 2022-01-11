# -*- coding: utf-8 -*-
"""
Created on Tue Jan 11 11:58:54 2022

@author: Unbeknownstguy
"""

import streamlit as st

st.title("Streamlit!")


checkbox_one = st.checkbox("Yes")
checkbox_two = st.checkbox("No")



if checkbox_one:
    value = "Yes"
elif checkbox_two:
    value = "No"
else:
    value = "No value selected"


st.write(f"You selected: {value}")


