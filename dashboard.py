from dash import Dash, html, dcc, callback, Output, Input
import dash_daq as daq
import plotly.express as px
import pandas as pd
import plotly
from plotly.subplots import make_subplots

df = pd.read_csv("netstats.csv")

app = Dash(__name__)

app.layout = html.Div([
    html.H1(children='Network Traffic Visualisation', style={'textAlign':'center'}),
    # Bar chart on web page
    dcc.Graph(id='live-update-graph'),
    # Gauge on web page
    daq.Gauge(
        id='h1-gauge',
        showCurrentValue=True,
        label="Host1 Avgerage Speed",
        units="MBps",
        max=50,
        min=0
    ),
    daq.Gauge(
        id='h2-gauge',
        showCurrentValue=True,
        label="Host2 Avgerage Speed",
        units="MBps",
        max=50,
        min=0
    ),
    dcc.Interval(
        id='interval-component',
        interval=5*1000,
        n_intervals=0
    )
])

@callback(Output('h1-gauge', 'value'), Input('interval-component', 'n_intervals'))
def update_metrics(n):
    df = pd.read_csv("netstats.csv")
    df_h1 = df.loc[df['Source'].isin(['host1'])]
    value = (df_h1['Size'].sum())/(5*1000)
    return value

@callback(Output('h2-gauge', 'value'), Input('interval-component', 'n_intervals'))
def update_metrics(n):
    df = pd.read_csv("netstats.csv")
    df_h2 = df.loc[df['Source'].isin(['host2'])]
    value = (df_h2['Size'].sum()/(5*1000))
    return value

@callback(Output('live-update-graph', 'figure'), Input('interval-component', 'n_intervals'))
def update_graph(n):
    df = pd.read_csv("netstats.csv")
    df_tcp = df.loc[df['Type'].isin(['tcp'])]
    df_udp = df.loc[df['Type'].isin(['udp'])]
    # fig = px.bar(df, x="Source", y="Size", color="Destination", barmode="group")
    fig = make_subplots(rows=1, cols=2, vertical_spacing=0.1, horizontal_spacing=0.25)
    fig.update_layout(
        autosize=False,
        width=1500,
        height=500
    )
    fig.append_trace({
        'x': df_tcp["Source"],
        'y': df_tcp["Size"],
        'type': 'bar',
        'name': 'tcp'
    }, 1, 1)
    fig.append_trace({
        'x': df_udp["Source"],
        'y': df_udp["Size"],
        'type': 'bar',
        'name': 'udp'
    }, 1, 2)
    return fig
if __name__ == '__main__':
    app.run(debug=True)
