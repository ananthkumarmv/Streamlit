# -*- coding: utf-8 -*-
"""
Created on Wed Jan 12 17:46:37 2022

@author: Unbeknownstguy
"""

import streamlit as st


# Displaying images

# importing image from pillow to open images
from PIL import Image
img = Image.open("Images/Eq.jpg")

# displaying image using streamlit
st.image(img, width=200)