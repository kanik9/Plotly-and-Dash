# Bubble charts :
"""

1. Bubble chart are very similar to scatter plots , except we now
   convey a third variable's information through the size of the
   markers.

2. We can also continue to add variable information by cloring
   points based on a category

"""

# Importing libraries
import pandas as pd
import plotly.offline as pyo
import plotly.graph_objs as go

# importing data set
df = pd.read_csv('/media/kanik/5DE14840704F5B09/Documents/Plotly-Dashboards-with-Dash-master/Data/mpg.csv')


data = [go.Scatter(x=df["horsepower"],
                   y=df['mpg'],
                   text=df['name'],
                   mode='markers',
                   marker=dict(size=df['weight']/100,
                                color=df['cylinders'],
                                showscale = True))]

layout = go.Layout(title="Bubble chart",hovermode='closest')

fig = go.Figure(data = data,layout = layout)
pyo.plot(fig,filename="Bubble_chart.html")
