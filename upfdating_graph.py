"""
1. In this section we are going to use 'hoverData','clickData','selectedData' on a graph to grab or to extract information of a specific part of
   graph.

   - 'hoverData' :  it i a property of graph which is use to see the information on a particular point when a user hover over the points
   - 'clickData' : it's a another property in which when a user click on a point then the information of clicked point is shown other wise
     'None'.
   - 'selectedData' : it shows the information or output of an operation which is held on a selected area only

2. All these property of graph are not decleared on dcc.graph ,it is decleared in Input or Output function  in callback .


"""

# Importing the libraries :
import dash
import pandas as pd
from numpy import random as rm
import plotly.graph_objs as go
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input , Output

#creating the app :
app = dash.Dash()

# Importing the dataset :
df = pd.read_csv("./Data/mpg.csv")
# Adding jitter of very less value
df['year'] = rm.randint(-4,5,len(df))*0.1+df['model_year']

# Creating the layout :

app.layout = html.Div([
                        html.Div([
                                    dcc.Graph(
                                               id='mpg-scatter',
                                               figure={
                                                        'data' :[
                                                                  go.Scatter(
                                                                              x=df['year']+1900,
                                                                              y=df['mpg'],
                                                                              text=df['name'],
                                                                              mode='markers'
                                                                            )
                                                                 ],
                                                        'layout' : go.Layout(
                                                                               title='MPG Data',
                                                                               xaxis={
                                                                                       'title' : 'Model Year'
                                                                                     },
                                                                               yaxis={
                                                                                       'title' : 'MPG'
                                                                                      },
                                                                               hovermode = 'closest'
                                                                             )
                                                      }
                                              )
                                   ],style={
                                               'width':'50%',
                                               'display':'inline-block'
                                           }
                        ),
                        html.Div([
                                   dcc.Graph(
                                               id='mpg_line',
                                               figure={
                                                        'data' :[
                                                                  go.Scatter(
                                                                              x=[0,1],
                                                                              y=[0,1],
                                                                              mode='lines'
                                                                            )
                                                                 ],
                                                        'layout' : go.Layout(
                                                                               title='Acceleration',
                                                                               margin={'l':0}
                                                                             )
                                                      }
                                            )
                                 ],
                                      style={
                                              'width' : '20%',
                                               'height': '50%',
                                               'display' : 'inline-block'
                                            }
                                 ),
                        html.Div([
                                   dcc.Markdown(id='mpg_stats')
                                 ],style={
                                          'width':'20%',
                                           'height':'50%',
                                           'display':'inline-block'
                                          }
                                )


                      ])

# Function
@app.callback(
               Output(component_id='mpg_line',component_property='figure'),
               [
                   Input(component_id='mpg-scatter',component_property='hoverData')
               ]
             )

def callback_graph(hoverData) :
    v_index = hoverData['points'][0]['pointIndex']
    figure = {
              'data':[
                         go.Scatter(
                                    x= [0,1],
                                    y=[0,60/df.iloc[v_index]['acceleration']],
                                    mode='lines',
                                    line = {
                                             'width' : 2*df.iloc[v_index]['cylinders']
                                           }
                                  )
                      ],
               'layout' : go.Layout(
                                      title = df.iloc[v_index]['name'],
                                      xaxis = {'visible':False},
                                      yaxis = {
                                                 'visible':False,
                                                  'range' :[0,60/df['acceleration'].min()]
                                               },
                                      margin={'l': 0},
                                      height=300
                                   )
    }

    return figure

@app.callback(
               Output(component_id='mpg_stats',component_property='children'),
               [
                   Input(component_id='mpg-scatter',component_property='hoverData')
               ]
             )

def callback_stats(hoverData):
    v_index = hoverData['points'][0]['pointIndex']
    stats = """
             {} cylinders
             {}cc displacement
             0 to 60mph in {} seconds
             """.format(
                        df.iloc[v_index]['cylinders'],
                        df.iloc[v_index]['displacement'],
                        df.iloc[v_index]['acceleration']
                       )

    return stats


# run server :
if __name__ == '__main__':
    app.run_server()

