# Importing the libraries :
import dash
import json
import base64
import pandas as pd
import plotly.graph_objs as go
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input,Output

# Importing the dataset :
df = pd.read_csv('./Data/wheels.csv')

# Creating the app :
app = dash.Dash()

# Function to load image
def encode_image(image_file):
    encoded = base64.b64encode(open(image_file, 'rb').read())
    return 'data:image/png;base64,{}'.format(encoded.decode())

# Create app layout:
app.layout = html.Div([
                        html.Div([
                                    dcc.Graph(
                                               id='wheels-plot',
                                               figure={
                                                        'data': [
                                                                   go.Scatter(
                                                                               x=df['color'],
                                                                               y=df['wheels'],
                                                                               dy=1, # this help to get grid like structure in graph
                                                                               mode = 'markers',
                                                                               marker={
                                                                                          'size' :15
                                                                                       }
                                                                             )
                                                                ],
                                                         'layout' : go.Layout(
                                                                                 title = "Test Dashboard",
                                                                                 xaxis = {
                                                                                           'title' : 'Colors'
                                                                                         },
                                                                                 yaxis = {
                                                                                           'title' : 'Wheels'
                                                                                         },
                                                                                 hovermode = 'closest'
                                                                              )
                                                       }
                                              )

                                 ],
                                   style={
                                            'width':'30%',
                                             'float' :'left'
                                         }
                                 ),
                        html.Div(
                                 [
                                   html.Img(id='hover-data',src='children',height=300)
                                 ],style={
                                           'paddingTop' : 35
                                          }
                                 ),
                        html.P(),

                        html.Div([
                                   html.Pre(id='json-data',
                                             style={
                                                     'paddingTop' :35,
                                                      'width' :'30%',
                                                      'float':'bottom'
                                                    }
                                            )
                                  ],
                                    style={
                                            'width':'30%',
                                             'float' :'bottom'
                                         })
])
# Setting the callback function to show json output :

@app.callback(
               Output(component_id='hover-data',component_property='src'),
               [
                   Input(component_id='wheels-plot',component_property='hoverData')
               ]
             )

# - hoverData is the property which belong to the any graph.


def callback_image(hoverData):

    wheel = hoverData['points'][0]['y']
    color = hoverData['points'][0]['x']
    path = '/home/kanik/PycharmProjects/covid-19/Data/Images/'
    return encode_image(path+df[(df['wheels'] == wheel) & (df['color'] == color)]['image'].values[0])



@app.callback(
               Output(component_id='json-data',component_property='children'),
               [
                   Input(component_id='wheels-plot',component_property='hoverData')
               ]
              )

def callback_json(hoverData):
    return json.dumps(hoverData, indent=2)

# run server :

if __name__ == '__main__':
    app.run_server()


