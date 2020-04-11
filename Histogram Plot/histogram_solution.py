
# Importing the libraries

import pandas as pd
import plotly.offline as pyo
import plotly.graph_objs as go

df = pd.read_csv("/media/kanik/5DE14840704F5B09/Documents/Plotly-Dashboards-with-Dash-master/Data/abalone.csv")

data = [go.Histogram(x=df['length'],
                          xbins=dict(start =0,
                                     end=1,
                                     size=0.02))]

layout = go.Layout(title="Shell lengths from the Abalone datset")

fig = go.Figure(data=data,layout=layout)

pyo.plot(fig,filename="histogram_solution.html")