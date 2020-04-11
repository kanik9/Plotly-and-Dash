# Importing the librries

import pandas as pd
import plotly.offline as pyo
import plotly.figure_factory as ff

df = pd.read_csv("/media/kanik/5DE14840704F5B09/Documents/Plotly-Dashboards-with-Dash-master/Data/iris.csv")


trace0 = df[df['class']=='Iris-setosa']['petal_length']
trace1 = df[df['class']=='Iris-versicolor']['petal_length']
trace2 = df[df['class']=='Iris-virginica']['petal_length']

hist_data = [trace0,trace1,trace2]
group_labels = ['Iris-setosa','Iris-versicolor','Iris-virginica']

fig = ff.create_distplot(hist_data,group_labels,bin_size=[0.2,0.1,0.3,0.4])
pyo.plot(fig,filename="distplot_solution.html")
