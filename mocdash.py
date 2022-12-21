import dash
from dash import Dash, dcc, html, Input, Output
import plotly.express as px
import pandas as pd

#Import data 
df = pd.read_csv("data/mocdash.csv")
fig = px.bar(df, x='Age', y='Likes')
app = dash.Dash()
server = app.server
app.layout = html.Div([
    html.H1("Social Media Dashboard"),
    dcc.Graph(figure=fig)
])

app.run_server(debug=True, use_reloader=False)  # Turn off reloader if inside Jupyter
