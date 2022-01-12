# -*- coding: utf-8 -*-
"""
Created on Wed Jan 12 18:20:11 2022

@author: Unbeknownstguy
"""

import streamlit as st

# multi select box
 
# first argument takes the box title
# second argument takes the options to show

hobbies = st.multiselect("Hobbies: ",
                         ['Dancing', 'Reading', 'Sports'])


# write the selected options
st.write("You selected", len(hobbies), 'hobbies')
