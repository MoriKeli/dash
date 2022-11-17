import dash
from dash.dependencies import Input, Output
import dash_core_components as dcc
import dash_html_components as html
app = dash.Dash()
# application layout
app.layout = html.Div([
    html.H1(
        children='First dash App!',
        style= {
            'textAlign': 'center',
            'color': '#456FBV'
        }
    
    ),
    html.Div(
        children='Dash - A data product development framework from plotly',
        style= {
            'textAlign': 'center',
            'color': '#BBFGT'
        }
    ),

    dcc.Graph(
        id = 'sample-graph',
        figure = {
            'data': [
                {
                    'x': [1, 2, 3, 4, 5, 6],
                    'y': [10, 20, 30, 40, 50, 120],
                    'type': 'bar',
                    'name': 'First bar'
                },
                {
                    'x': [1, 2, 3, 4, 5, 6],
                    'y': [50, 5, 80, 100, 20, 35],
                    'type': 'bar',
                    'name': 'Second bar'
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