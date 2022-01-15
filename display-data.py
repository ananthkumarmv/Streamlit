# -*- coding: utf-8 -*-
"""
Created on Sat Jan 15 20:44:43 2022

@author: Unbeknownstguy
"""

import streamlit as st
import numpy as np
import pandas as pd
st.title('This is my first app!')
st.write('This is a table')

dataframe = pd.DataFrame(np.random.randn(10, 20),
            columns = ('col %d' % i
                       for i in range(20)))
# we can use "dataframe" directly instead of using
# st.write(dataframe). This is called as magical command
st.write(dataframe) 
