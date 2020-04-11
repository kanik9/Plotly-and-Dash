#######
# Objective: Create a dashboard that takes in two or more
# input values and returns their product as the output.
######

# Perform imports here:
import dash
import dash_html_components as html
import dash_core_components as dcc
from dash.dependencies import Input, Output


# Launch the application:

app = dash.Dash()


# Create a Dash layout that contains input components
# and at least one output. Assign IDs to each component:

app.layout = html.Div([
                        dcc.RangeSlider(
                                          id='range',
                                          min=-5,
                                          max=6,
                                          value=[-3,4],
                                          marks={i : i for i in range(-5,7)}
                                        ),
                        html.Div(id='answer')
                     ])



# Create a Dash callback:

@app.callback(
               Output(component_id='answer',component_property='children'),
               [Input(component_id='range',component_property='value')]
            )
def multiply(list_value):
    return list_value[0]*list_value[1]



# Add the server clause:

if __name__ == "__main__":
    app.run_server()
