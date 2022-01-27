from app import app
from flask import render_template
# import dash
# import dash_core_components as dcc
# import dash_html_components as html
# from dash.dependencies import Input, Output
# import plotly.express as px


# from dash.dependencies import Input, Output
# import plotly.graph_objects as go

# app = dash.Dash(__name__)

# app.layout = html.Div([
#     html.P("Color:"),
#     dcc.Dropdown(
#         id="dropdown",
#         options=[
#             {'label': x, 'value': x}
#             for x in ['Gold', 'MediumTurquoise', 'LightGreen']
#         ],
#         value='Gold',
#         clearable=False,
#     ),
#     dcc.Graph(id="graph"),
# ])


@app.route('/')
def home():
    return render_template('index.html')

# @app.callback(
#     Output("graph", "figure"), 
#     [Input("dropdown", "value")])
# def display_color(color):
#     fig = go.Figure(
#         data=go.Bar(y=[2, 3, 1], marker_color=color))
#     return render_template('piechart.html',fig=fig)

# app.run_server(debug=True)



