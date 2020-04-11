# Importing the libraries

import pandas as pd
import plotly.offline as pyo
import plotly.graph_objs as go

df = pd.read_csv("/media/kanik/5DE14840704F5B09/Documents/Plotly-Dashboards-with-Dash-master/Data/mpg.csv")

data = [go.Histogram(x=df['mpg'],
                     xbins=dict(start=0,
                                end=50,
                                size=2))]

layout = go.Layout(title='Histogram')
fig = go.Figure(data = data,layout=layout)
pyo.plot(fig,filename='histogram.html')