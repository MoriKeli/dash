import dash
from dash.dependencies import Input, Output
import dash_core_components as dcc
import dash_html_components as html
from pandas_datareader import data as web
# import pandas as pd
from datetime import datetime

app = dash.Dash()
app.layout = html.Div([
    dcc.Dropdown(
        id='dropdown',
        options = [
            {'label': 'Jersey  No. 10', 'value': 10},
            {'label': 'Team: Chelsea', 'value': 'chelsea'},
        ],
        value=10,
    ),
    dcc.Graph(id='graph'),

])


@app.callback(Output('graph', 'figure'), [Input('dropdown', 'value')])
def display_graph(players_profile):
    df = web.DataReader(players_profile, 'Chelsea', datetime(2014, 1, 1), datetime.now())

    return {
        'data': [
            {
                'x': df.Club,
                'y': df.Potential,
            }],
        'layout': {'margin': {'l': 40, 'r': 0, 't': 20, 'b': 30}},
    }



if __name__ == '__main__':
    app.run_server(debug=True)