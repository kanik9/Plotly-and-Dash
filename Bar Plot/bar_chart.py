# Bar Chart :

"""

A bar chart presents Categorical data with rectangular bars with heights (or lengths) proportional to the values that
they represent

* Using Bar Charts, we can visualize categorical data

* Typically the x-axis is the categories and the y-axis is the count(number of occurrences) in each category

* However the y-axis can be any aggregation : count , sum ,average etc.

"""

#Importing Important libraies

import pandas as pd
import plotly.offline as pyo
import plotly.graph_objs as go

# Importing data by using pands
data = pd.read_csv("/media/kanik/5DE14840704F5B09/Documents/Plotly-Dashboards-with-Dash-master/Data/2018WinterOlympics.csv")
#print(data)


# Bar Chart:


trace = go.Bar(x=data["NOC"],
               y=data["Total"])

data_bar = [trace]
layout_bar = go.Layout(title='Total Number of Medals')

fig_bar = go.Figure(data=data_bar,layout=layout_bar)
pyo.plot(fig_bar,filename='bar_chart.html')




# Nested Bar Chart



trace_gold = go.Bar(x=data["NOC"],
               y=data["Gold"],
               name='Gold',
               marker = {'color':'#FFD700'})

trace_silver = go.Bar(x=data["NOC"],
               y=data["Silver"],
               name='Silver',
               marker = {'color':'#9EA0A1'})

trace_bronze = go.Bar(x=data["NOC"],
               y=data["Bronze"],
               name='Bronze',
               marker = {'color':'#CD7F32'})



data_nested = [trace_gold,trace_silver,trace_bronze]
layout_nested = go.Layout(title='Specific Bar Graph of gold , silver and bronze')

fig_nested = go.Figure(data=data_nested,layout=layout_nested)
pyo.plot(fig_nested,filename='nested_bar_chart.html')



# Stacked Bar Chart




trace1_gold = go.Bar(x=data["NOC"],
               y=data["Gold"],
               name='Gold',
               marker = {'color':'#FFD700'})

trace1_silver = go.Bar(x=data["NOC"],
               y=data["Silver"],
               name='Silver',
               marker = {'color':'#9EA0A1'})

trace1_bronze = go.Bar(x=data["NOC"],
               y=data["Bronze"],
               name='Bronze',
               marker = {'color':'#CD7F32'})



data_stacked = [trace1_gold,trace1_silver,trace1_bronze]
layout_stacked = go.Layout(title='Specific Bar Graph of gold , silver and bronze in a single bar',
                           barmode='stack')

fig_stacked = go.Figure(data=data_stacked,layout=layout_stacked)
pyo.plot(fig_stacked,filename='stacked_bar_chart.html')

