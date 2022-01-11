# -*- coding: utf-8 -*-
"""
Created on Tue Jan 11 12:08:21 2022

@author: Unbeknownstguy
"""

import streamlit as st
import plotly.graph_objs as go


st.title("Streamlit!")

fig = go.Figure(
    data=[go.Pie(
        labels=['A', 'B', 'C'],
        values=[30, 20, 50]
    )]
)
fig = fig.update_traces(
    hoverinfo='label+percent',
    textinfo='value',
    textfont_size=15
)

st.write("Pie chart in Streamlit")
st.plotly_chart(fig)
