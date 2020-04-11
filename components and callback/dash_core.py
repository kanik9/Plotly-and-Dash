# Importing the libraries :

import dash
import dash_html_components as html
import dash_core_components as dcc


# Creating app
app = dash.Dash()

# Workarea
app.layout = html.Div([
                          html.P(html.Label('Dropdown')),
                          dcc.Dropdown(
                                        options=[
                                                  {'label': 'New York City', 'value': 'NYC'},
                                                  {'label': 'Montréal', 'value': 'MTL'},
                                                  {'label': 'San Francisco', 'value': 'SF'}
                                                ],
                                        value='MTL'
                                       ),
                          html.P(html.Label("Slider")),
                          dcc.Slider(min=-10,
                                      max=10,
                                      #step=3,
                                      value=0,
                                      marks={i:i for i in range(-10,11)}),

                          html.P(html.Label('Some Radio Items')),
                          dcc.RadioItems(
                                          options=[
                                                    {'label':'New York City', 'value': 'NYC'},
                                                    {'label': 'Montréal', 'value': 'MTL'},
                                                    {'label': 'San Francisco', 'value': 'SF'}
                                                  ],
                                          value='MTL'
                                        )

                      ])

# Run Server :

if __name__ == '__main__' :
    app.run_server()