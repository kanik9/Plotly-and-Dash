# Importing the libraries

import numpy as np
import pandas as pd
import plotly.offline as pyo
import plotly.graph_objs as go

# importing the dataset using pandas

loc = "/media/kanik/5DE14840704F5B09/Documents/Plotly-Dashboards-with-Dash-master/Data/abalone.csv"
data = pd.read_csv(loc)

x = np.random.choice(data['rings'],30,replace = False)
y = np.random.choice(data['rings'],100,replace = False)

trace = [go.Box(y = x,name = 'A'),
         go.Box(y=y,name="B")]

layout = go.Layout(title = 'Comparison of two samples taken from the same population')

fig = go.Figure(data=trace,layout= layout)
pyo.plot(fig,filename='box_plot_solution.html')