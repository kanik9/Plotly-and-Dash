# Importing the Libraries :

import dash
import numpy as np
import dash_html_components as html
import dash_core_components as dcc
import plotly.graph_objs as go

# Creating app

app = dash.Dash()

# Creating dataset
np.random.seed(42)
x_value = np.random.randint(1,101,100)
y_value = np.random.randint(1,101,100)

app.layout = html.Div([
                        dcc.Graph(
                                  id='Scatter Plot 1',
                                  figure = {'data':[
                                                    go.Scatter(x=x_value,
                                                               y=y_value,
                                                               mode = 'markers',
                                                               marker = {
                                                                           'size' : 12,
                                                                            'color':'rgb(51,204,153)',
                                                                            'symbol' : 'pentagon',
                                                                            'line' : {
                                                                                       'width' : 2
                                                                                     }
                                                                         }
                                                               )
                                                  ],
                                            'layout':go.Layout(
                                                                title='Scatter Plot 1',
                                                                xaxis= {
                                                                         "title" : 'Some X Tiles'
                                                                        }
                                                              )

                                           }
                                )
                      ,dcc.Graph(
                                   id='Scatter Plot 2',
                                   figure={'data': [
                                                    go.Scatter(x=x_value,
                                                               y=y_value,
                                                               mode='markers',
                                                               marker={
                                                                        'size': 12,
                                                                        'color': 'rgb(255,0,0)',
                                                                        'symbol': 'circle',
                                                                        'line': {
                                                                                  'width': 2
                                                                                 }
                                                                       }
                                                              )
                                                    ],
                                            'layout': go.Layout(
                                                                 title='Scatter Plot 2',
                                                                 xaxis={
                                                                         "title": 'Some X Tiles'
                                                                       }
                                                                )

                                           }
                               )
                    ])



if __name__ == '__main__':
    app.run_server()