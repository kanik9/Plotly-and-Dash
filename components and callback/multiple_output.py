# Importing the Libraries :

import dash
import pandas as pd
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input,Output
import base64


df = pd.read_csv("./wheels.csv")

app = dash.Dash()

def encode_image(image_file):
    encoded = base64.b64encode(open(image_file,'rb').read())
    return 'data :image/png;base64,{}'.format(encoded.decode())

app.layout = html.Div([
                         html.Div([
                                   dcc.RadioItems(
                                                   id='radio-button-number',
                                                   options=[
                                                             {'label':i,'value':i} for i in df['wheels'].unique()
                                                           ],
                                                   value=1
                                                  ),
                                   html.Div(id='answer1')
                                  ]
                                ),
                         html.Hr(),
                         html.Div([
                                    dcc.RadioItems(
                                                    id='radio-button-color',
                                                    options=[
                                                               {'label':i,'value':i} for i in df['color'].unique()
                                                             ],
                                                    value='blue '
                                                  ),
                                    html.Div(id='answer2')
                                  ]),
                         html.Img(id='display-image',src='children',height=300)
                      ],style={
                               'fontFamily' : 'helvetica',
                                'fontSize' :18
                               }
                     )

@app.callback(
                Output(component_id='answer1',component_property='children'),
                [Input(component_id='radio-button-number',component_property='value')]
              )

def update_output_div_number(input_value):
    return "You've Selected :{}".format(input_value)

@app.callback(
                Output(component_id='answer2',component_property='children'),
                [Input(component_id='radio-button-color',component_property='value')]
              )

def update_output_div_color(input_color):
    return "You've Selected :{}".format(input_color)


@app.callback(
                Output(component_id='display-image',component_property='src'),
                [
                 Input(component_id='radio-button-number',component_property='value'),
                 Input(component_id='radio-button-color',component_property='value')
                ]
             )


def callback_image(wheel,color):
    path ='./Images/'
    return encode_image(path+df[(df['wheels'] == wheel) & (df['color'] == color)]['image'].values[0])


if __name__ == '__main__':
    app.run_server()