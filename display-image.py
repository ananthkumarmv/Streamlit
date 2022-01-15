# -*- coding: utf-8 -*-
"""
Created on Sat Jan 15 21:00:43 2022

@author: Unbeknownstguy
"""


import streamlit as st
from PIL import Image

image = Image.open('picture.jpg')
st.image(image, caption = 'This is a picture', use_column_width = True)

