#Importing Important libraies

import pandas as pd
import plotly.offline as pyo
import plotly.graph_objs as go

# Importing the data by using pandas
 
data = pd.read_csv("/media/kanik/5DE14840704F5B09/Documents/Plotly-Dashboards-with-Dash-master/SourceData/nst-est2017-alldata.csv")
#print(data)

# Data Cleaning from a large set of data
data2 = data[data["DIVISION"] == '1']
data2.set_index('NAME',inplace=True)

list_of_pop_col = [col for col in data2.columns if col.startswith("POP")]
data2 = data2[list_of_pop_col]

#print(data2)

data = [go.Scatter(x=data2.columns,
                   y=data2.loc[name],
                   mode='lines',
                   name=name) for name in data2.index]

pyo.plot(data,filename='line_chart_with_pandas.html')