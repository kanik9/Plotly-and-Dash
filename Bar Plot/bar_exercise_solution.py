#Importing Important libraies

import pandas as pd
import plotly.offline as pyo
import plotly.graph_objs as go

# Importing data using pandas

data = pd.read_csv("/media/kanik/5DE14840704F5B09/Documents/Plotly-Dashboards-with-Dash-master/Data/mocksurvey.csv")
print(data)

trace1 = go.Bar(x=data.index,
                y=data["Strongly Agree"],
                name='Strongly Agree',
                marker={'color' : 'blue'})

trace2 = go.Bar(x=data.index,
                y=data["Somewhat Agree"],
                name='Somewhat Agree',
                marker={'color' : 'orange'})

trace3 = go.Bar(x=data.index,
                y=data["Neutral"],
                name='Neutral',
                marker={'color' : 'green'})

trace4 = go.Bar(x=data.index,
                y=data["Somewhat Disagree"],
                name='Somewhat Disagree',
                marker={'color' : 'red'})

trace5 = go.Bar(x=data.index,
                y=data["Strongly Disagree"],
                name='Strongly Disagree',
                marker ={'color' : 'purple'})

"""

data = [go.Bar(
    x = df.index,
    y = df[response],
    name=response
) for response in df.columns]

"""

trace = [trace1,trace2,trace3,trace4,trace5]

layout = go.Layout(title = 'Mock Survey Result',
                   barmode='stack')

fig = go.Figure(data=trace, layout=layout)
pyo.plot(fig,filename='bar_solution.html')
