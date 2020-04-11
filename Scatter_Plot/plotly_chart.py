#Importing Important libraies

import numpy as np
import plotly.offline as pyo
import plotly.graph_objs as go

# Scatter plot
"""
1. A Scatter plot displays a series of data points (markers) or in 
   Scatter way.
   In Scatter plot points are random not in a series
"""

np.random.seed(42)
random_x = np.random.randint(1,101,100)
random_y = np.random.randint(1,101,100)

# Method 1


data = [go.Scatter(x=random_x , y=random_y, mode='markers')]

pyo.plot(data ,filename='scatter.html')


# Method 2
"""
In this method we explain how to add titles by 
using layout function of plotly.graph_objs library 
"""


data = [go.Scatter(x=random_x , y=random_y, mode='markers')]
layout = go.Layout(title='Hello First plot',
                    xaxis={'title':'My X axix'},
                    yaxis=dict(title='My Y axix'),
                    hovermode='closest')
fig = go.Figure(data=data,layout = layout)
pyo.plot(fig,filename='scatter_1.html')

# Method 3

"""
In this method we explain how to coustmize the points shape and color
with the titles in graph

"""

data = [go.Scatter(x=random_x,
                   y=random_y,
                   mode='markers',
                   marker=dict(
                       size=12,
                       color='rgb(51,204,153)',
                       symbol='pentagon',
                       line={'width':2}
                   ))]


layout = go.Layout(title='Hello First plot',
                    xaxis={'title':'My X axix'},
                    yaxis=dict(title='My Y axix'),
                    hovermode='closest')
fig = go.Figure(data=data,layout = layout)
pyo.plot(data ,filename='scatter_2.html')

