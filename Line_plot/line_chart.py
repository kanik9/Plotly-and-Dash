#Line chart

"""

1. A line chart displays a series of data points (markers) connected by line segment .
2. It is similar to a scatter plot except that the measurement points are ordered (typically by their x-axis value) are
   joined with straight line segments.
3. Often used to visualize a trend in data over intervals of time known as time series


"""

#Importing Important libraies

import numpy as np
import plotly.offline as pyo
import plotly.graph_objs as go



np.random.seed(56)

x_value = np.linspace(0, 1, 100)
y_value = np.random.randn(100)

# Markers :

trace = go.Scatter(x=x_value,
                   y=y_value + 5,
                   mode='markers',
                   name='markers'
                   )

# Normal Line :
trace_line = go.Scatter(x=x_value,
                        y=y_value,
                        mode="lines",
                        name='myline')

# Line with Markers :
trace_mix = go.Scatter(x=x_value,
                        y=y_value-5,
                        mode="lines+markers",
                        name='Mix')

"""
By using trace you can add multiple graphs in a single
graphs

In this trace , it is a graph which shows markers
at y = y+5
After the trace i added a another graph which shows 
line graphs 
In the trace_mix a graph shows the combine figure of trace and trace_line
  
"""


data_line = [trace,trace_line,trace_mix]
layout_line = go.Layout(title='Line Chart')


fig_line = go.Figure(data=data_line, layout=layout_line)
pyo.plot(fig_line,filename='line_chart.html')









