#Importing Important libraies

import pandas as pd
import plotly.offline as pyo
import plotly.graph_objs as go

# Importing data using pandas

df = pd.read_csv("/media/kanik/5DE14840704F5B09/Documents/Plotly-Dashboards-with-Dash-master/Data/mocksurvey.csv",index_col = 0)
print(df)

data = [go.Bar(
    y=df.index,
    x=df[response],
    orientation='h',
    name=response
) for response in df.columns]

layout = go.Layout(title = 'Mock Survey Result',
                   barmode='stack')

fig = go.Figure(data=data, layout=layout )
pyo.plot(fig,filename='bar_solution2.html')
