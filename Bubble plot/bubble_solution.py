# Importing libraries
import pandas as pd
import plotly.offline as pyo
import plotly.graph_objs as go

# importing data set
df = pd.read_csv('/media/kanik/5DE14840704F5B09/Documents/Plotly-Dashboards-with-Dash-master/Data/mpg.csv')

data =[go.Scatter(x=df['displacement'],
                  y=df['acceleration'],
                  text=df['name'],
                  mode='markers',
                  marker = dict(size=df['weight']/500))]

layout = go.Layout(title='Vehicle acceleration vs. displacement',
                   xaxis=dict(title='displacement'),
                   yaxis=dict(title='acceleration = seconds to reach 60mph'),
                   hovermode='closest')

fig = go.Figure(data=data,layout=layout)
pyo.plot(fig,filename='Bubble_chart_solution.html')
