import dash
import pandas as pd
from datetime import datetime
import pandas_datareader.data as web
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input,Output,State

app = dash.Dash()

nsdq = pd.read_csv('./Data/NASDAQcompanylist.csv')
nsdq.set_index('Symbol',inplace=True)

options = []
for tic in nsdq.index:
    mydict = {}
    mydict['label'] = nsdq.loc[tic]['Name']+' '+tic  # = Apple co. == AAPl
    mydict['value'] = tic
    #{'label':'user sees','value':'script sees }
    options.append((mydict))

app.layout = html.Div([
                        html.H1('Stock Ticker Dashboard'),
                        html.Div([
                                    html.H3('Enter a stock symbol:'),
                                    dcc.Dropdown(
                                                id='my_stock_ticker',
                                                options=options,
                                                value='TSLA', # sets a default value
                                                multi=True

                                               )
                                   ],
                                     style={
                                             'display' : 'inline-block',
                                              'verticalAlign':'top',
                                              'width' : '30%'
                                           }
                                 ),
                        html.Div([
                                  html.H3('Select a start and end date :'),
                                  dcc.DatePickerRange(
                                                       id='date-select',
                                                       #start_date_placeholder_text='Start Period',
                                                       min_date_allowed=datetime(2015,1,1),
                                                       max_date_allowed=datetime.today(),
                                                       start_date= datetime(2018,1,1),
                                                       #end_date_placeholder_text="End Period",
                                                       end_date = datetime.today(),
                                                       #calendar_orientation='vertical'
                                                      )
                                ], style={
                                           # 'width' : "45%",
                                            'display' : 'inline-block',
                                            #'paddingLeft' : 30

                                         }
                               ),
                        html.Div([
                                   html.Button(
                                                id='submit-button',
                                                n_clicks=0,
                                                children='Submit',
                                                style={
                                                       'fontSize' : 24,
                                                        'marginLeft':'30px'
                                                     }
                                               )
                                 ],
                                   style={
                                         "display" : 'inline-block'
                                         }
                               ),
                        dcc.Graph(
                                   id='my_graph',
                                   figure={
                                            'data': [
                                                      {'x': [1,2], 'y': [3,1]}
                                                     ]
                                            #'layout' : {'title':'Default title'}
                                           }
                                  )
                       ])



@app.callback(
               Output(component_id='my_graph',component_property='figure'),
               [
                 Input(component_id='submit-button',component_property='n_clicks')
               ],
               [
                   State(component_id='my_stock_ticker',component_property='value'),
                   State(component_id='date-select',component_property='start_date'),
                   State(component_id='date-select',component_property='end_date')
               ]
            )

def update_graph(n_clicks,stock_ticker,start_date,end_date):
    start = datetime.strptime(start_date[:10],'%Y-%m-%d')
    end = datetime.strptime(end_date[:10],'%Y-%m-%d')
    #df = web.DataReader(stock_ticker,'iex' ,start,end)
    traces = []

    for tic in stock_ticker:
        df = web.DataReader(tic,'iex',start,end)
        traces.append({'x':df.index,'y':df['close'],'name':tic})

    fig = {
            'data':[
                     traces
                   ],
            'layout' : {'title':stock_ticker}
          }
    return fig








if __name__ == '__main__':
    app.run_server()
