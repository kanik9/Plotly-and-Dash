import dash
import dash_html_components as html

app = dash.Dash()

app.layout = html.Div(['This is the Outermost Div!',
                      html.Div(['This is an inner Div cell!'],
                               style={
                                        'color':'red',
                                        'border' :'2px black solid '
                                     }),
                       html.Div(['Another inner Div'],
                                style={
                                        'color': 'gray',
                                        'border' : '4px gray solid'
                                      })],
                      style={ 
                              'color' : 'green',
                              'border': '6px green solid',
                              'margin': '2px'
                            })


if __name__ == "__main__" :
    app.run_server()