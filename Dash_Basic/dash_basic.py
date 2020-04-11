import dash
import dash_core_components as dcc
import dash_html_components as html


"""
We can build the layout with the dash_html_components library and the dash_core_components library. I have imported them 
as shown above. 
The dash_html_components is for all HTML tags, whereas the latter one is for interactive components built with React.js.
Having said that,let’s write something in our browser using Dash:

"""

"""
Notice the children attribute in the first Div . It is used to define the list of elements enclosed in that tag. This is a positional argument 
(always comes first) and can be skipped as you can see in the next H1 and Div shown above

<div>
 <h1> Hello Dash </h1>
 <div> Dash : Web Dashboard with Python </div>
</div>
"""
app = dash.Dash()

colors = {'background' : '#111111','text' : '#7FDBFF'}


app.layout = html.Div(children=[
    html.H1(children ="Hello Dash !",style={'textAlign': 'center',
                                            'color': colors['text']
                                            }
            ),
    dcc.Graph(id = 'example',
              figure={'data':[
                                {'x':[1,2,3,4],'y': [5,6,7,8],'type': 'bar', 'name': 'SF'},
                                {'x':[1,2,3,4],'y' : [9,10,11,12],'type':'bar','name': 'NYC'}
                              ],
                       'layout':{
                                   'plot_bgcolor':colors['background'],
                                   'paper_bgcolor': colors['background'],
                                   'font': {'color':colors['text']},
                                   'title':'Bar Plots!'
                                }
                     }
              )
                                ],
    style = {
              'background' :colors['background']
            }

                        )

if __name__ == '__main__':
    app.run_server()