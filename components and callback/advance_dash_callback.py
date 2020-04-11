
# Importing the libraries

import dash
import pandas as pd
import dash_html_components as html
import dash_core_components as dcc
import plotly.graph_objs as go
from dash.dependencies import Input, Output


# Importing the dataset

df = pd.read_csv('./gapminderDataFiveYear.csv')
"""
df =        country    year      pop     continent  lifeExp  gdpPercap
       0  Afghanistan  1952   8425333.0      Asia   28.801  779.445314
       1  Afghanistan  1957   9240934.0      Asia   30.332  820.853030
       2  Afghanistan  1962  10267083.0      Asia   31.997  853.100710
       3  Afghanistan  1967  11537966.0      Asia   34.020  836.197138
       4  Afghanistan  1972  13079460.0      Asia   36.088  739.981106
"""

# Creating the app
app = dash.Dash()

year_option = []
for year in df['year'].unique():
    year_option.append({'label':str(year),'value':year})


app.layout = html.Div([
                        dcc.Graph(
                                   id='graph',
                                  ),
                        dcc.Dropdown(
                                       id='year-picker',
                                       options= year_option,
                                       value = df['year'].min()
                                     )
                      ])
@app.callback(
                Output(component_id='graph',component_property='figure'),
                [Input(component_id='year-picker',component_property='value')]
              )

def update_figure(selected_year):

    filtered_df = df[df['year'] == selected_year ]
    traces = []

    for continent_name in filtered_df['continent'].unique():
        df_by_continent = filtered_df[filtered_df['continent'] == continent_name]
        traces.append(go.Scatter(
                                  x=df_by_continent['gdpPercap'],
                                  y=df_by_continent['lifeExp'],
                                  mode='markers',
                                  opacity = 0.7,
                                  marker = {
                                             'size' : 12
                                           },
                                  name = continent_name

                                )
                     )

    return {
             'data' : traces,
             'layout' : go.Layout(title='My Plot',
                                  xaxis={
                                          'title': 'GDP Per Cap','type' : 'log'
                                        },
                                  yaxis={
                                           'title' : 'Life Expectancy'
                                        }
                                  )
           }


if __name__ == '__main__':
    app.run_server()

