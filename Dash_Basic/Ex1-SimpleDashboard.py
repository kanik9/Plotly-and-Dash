#######
# Objective: build a dashboard that imports OldFaithful.csv
# from the data directory, and displays a scatterplot.
# The field names are:
# 'D' = date of recordings in month (in August),
# 'X' = duration of the current eruption in minutes (to nearest 0.1 minute),
# 'Y' = waiting time until the next eruption in minutes (to nearest minute).
######

# Perform imports here:
import dash
import pandas as pd
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objs as go


# Launch the application:

app = dash.Dash()


# Create a DataFrame from the .csv file:
dataframe = pd.read_csv("./OldFaithful.csv")
x_values = dataframe['X']
y_values = dataframe['Y']


# Create a Dash layout that contains a Graph component:
app.layout = html.Div([
                        dcc.Graph(
                                   id = 'Practice Class',
                                   figure = {
                                              'data' :[
                                                        go.Scatter(
                                                                    x = x_values,
                                                                    y = y_values,
                                                                    mode = 'markers',
                                                                    marker = {
                                                                               'size': 12,
                                                                                'color':'rgb(0,255,0)',
                                                                                'symbol':'circle',
                                                                             }
                                                                  )
                                                      ],
                                               'layout': go.Layout(
                                                                    title = 'Old Faithful Eruption Intervals Vs Duration',
                                                                    xaxis ={ 'title': 'Duration of the current eruption in minutes (to nearest 0.1 minute)'},
                                                                    yaxis = {'title': 'Waiting time until the next eruption in minutes (to nearest minute)'}
                                                                  )
                                            }
                                 )
                      ])




# Add the server clause:

if __name__ == '__main__':
    app.run_server()
