
# Importing the libraries :
import dash
import pandas as pd
import plotly.graph_objs as go
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input,Output

# importing the dataset in it :

df = pd.read_csv("./mpg.csv")

# Creating app

app = dash.Dash()


#['mpg','hp','displace'...]

features = df.columns

# Creating layout :

app.layout = html.Div([
                        html.Div([
                                   dcc.Dropdown(id='xaxis',
                                               options=[
                                                        {'label':i ,'value' :i}for i in features
                                                       ],
                                               value = 'displacement'
                                               )
                                 ],style={
                                           'width' : '48%',
                                            'display': 'inline-block'
                                         }
                                ),
                        html.Div([
                                   dcc.Dropdown(
                                                 id='yaxis',
                                                 options=[
                                                        {'label':i ,'value' :i}for i in features
                                                       ],
                                                 value = 'mpg'
                                               )
                                 ],style={
                                           'width' : '48%',
                                            'display': 'inline-block'
                                         }
                                 ),
                        dcc.Graph(id='feature-graphic')
                      ],style={
                                'padding':10
                              }
                     )

# Callback function :
@app.callback(
               Output(component_id='feature-graphic',component_property='figure'),
              [
               Input(component_id='xaxis',component_property='value'),
               Input(component_id='yaxis',component_property='value')
              ]
             )

# Update function :

def update_graph(xaxis_name,yaxis_name) :
    return {
             'data' :[
                       go.Scatter(x=df[xaxis_name],
                                  y=df[yaxis_name],
                                  mode='markers',
                                  text=df['name'],
                                  marker = {
                                             'size':15,
                                             'opacity':0.5,
                                             'line' :{
                                                       'width':0.5,
                                                        'color':'red'
                                                     }

                                           }
                                 )
                     ],
             'layout':go.Layout(
                                 title ='My Dashboard for MPG',
                                 xaxis = {
                                           'title':'xaxis_name'
                                         },
                                 yaxis = {
                                           'title' : 'yaxis_name'
                                         },
                                 hovermode='closest'
                               )
           }

# Main Server :

if __name__ == '__main__':
    app.run_server()