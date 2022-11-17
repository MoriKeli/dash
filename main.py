import dash
from dash.dependencies import Input, Output
import dash_core_components as dcc
import dash_html_components as html
app = dash.Dash()
# application layout
app.layout = html.Div([
    html.H1('First dash App!'),
    html.Div('Dash - A data product development framework from plotly'),

    dcc.Graph(
        id = 'sample-graph',
        figure = {
            'data': [
                {
                    'x': [1, 2, 3, 4, 5],
                    'y': [10, 20, 30, 40, 50, 60],
                    'type': 'bar',
                    'name': 'Simple bar chart'
                }    
            ],
            'layout': {
                'title': 'Simple bar chart',
            }

        },
    )

])
if __name__ == '__main__':
    app.run_server(debug=True)