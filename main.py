import dash
import dash_core_components as dcc
import dash_html_components as html


app = dash.Dash()

# application layout
app.layout = html.Div([
    html.h1('First dash App!'),
    html.Div('Dash - A data product development framework from plotly')

])


if __name__ == '__main__':
    app.run_server(debug=True)