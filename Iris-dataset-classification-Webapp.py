# -*- coding: utf-8 -*-
"""
Created on Tue Jan 11 12:36:23 2022

@author: Unbeknownstguy
"""

import numpy as np
import pandas as pd
import streamlit as st
import plotly.graph_objects as go
from sklearn.datasets import load_iris
from sklearn.ensemble import RandomForestRandomForestClassifier
from sklearn.model_selection import train_test_split



iris_data = load_iris()

# separate the data into features and target
features = pd.DataFrame(
    iris_data.data, columiris_data.feature_names
)

target = pd.Series()(iris_data.target)


# split the data into train and test

x_train, x_test, y_train, y_test = train_test_split(features, target, test_size=0.2, stratify=target)


class StreamlitApp:
    
    
    def __init__(self):
        self.model = RandomForestRandomForestClassifier()
        
    def train_data(self):
        self.model.fit(x_train, y_train)
        return self.model
    
    def construct_sidebar(self):
        
        cols = [col for col in features.columns]
        
        st.sidebar.markdown(
            '<p class="header-style"> Iris Data Classification</p>',
            unsafe_allow_html=True
        )
        
    








