import dash
from dash import Dash, dcc, html, Input, Output
import plotly.express as px
import pandas as pd
from jupyter_dash import JupyterDash

df = pd.read_csv("data/mocdash.csv")

fig1 = px.scatter(df, x="Likes", y="Service", color="Gender",
                 size='Likes', hover_data=['Gender'])
fig2 = px.bar(df, x='Age', y='Likes')
fig3 = px.histogram(df, x='Service', y='Likes', color='Gender')

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

server = app.server

app.layout = html.Div(children=[
    # All elements from the top of the page
    html.Div([
        html.Div([
            html.H2(children='Distribution by Gender'),
            dcc.Graph(id='graph1', figure=fig1),
        ], className='six columns'),
        
        html.Div([
            html.H2(children='Disbribution Ages by Like'),
            dcc.Graph(id='graph2', figure=fig2),
        ], className='six columns'),
    ], className='row'),
    # New Div for all elements in the new 'row' of the page
    html.Div([
        html.H2(children='Distribution Services by Likes'),
        dcc.Graph(id='graph3', figure=fig3),
    ], className='row'),
])

    
    
app.run_server(debug=True, use_reloader=False)  # Turn off reloader if inside Jupyter