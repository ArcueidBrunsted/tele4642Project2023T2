from dash import Dash, html, dcc, callback, Output, Input
import dash_daq as daq
import plotly.express as px
import pandas as pd
import plotly
from plotly.subplots import make_subplots
import plotly.graph_objects as go

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
        label="Host1 Average Speed",
        units="MBps",
        max=150,
        min=0
    ),
    daq.Gauge(
        id='h2-gauge',
        showCurrentValue=True,
        label="Host2 Average Speed",
        units="MBps",
        max=150,
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
    df_h1 = df.loc[df['src_ip_addr'].isin(['10.0.0.1'])]
    value = (df_h1['# of bytes'].sum())/(15*1024)
    return value

@callback(Output('h2-gauge', 'value'), Input('interval-component', 'n_intervals'))
def update_metrics(n):
    df = pd.read_csv("netstats.csv")
    df_h2 = df.loc[df['src_ip_addr'].isin(['10.0.0.2'])]
    value = (df_h2['# of bytes'].sum()/(15*1024))
    return value

@callback(Output('live-update-graph', 'figure'), Input('interval-component', 'n_intervals'))
def update_graph(n):
    df = pd.read_csv("netstats.csv")
    df_tcp = df.loc[df['Protocol'].isin(['TCP'])]
    df_udp = df.loc[df['Protocol'].isin(['UDP'])]
    fig = make_subplots(rows=2, cols=2, vertical_spacing=0.1, horizontal_spacing=0.25)
    fig.update_layout(
        autosize=False,
        width=1200,
        height=500
    )
    df_h1_tcp = df_tcp.loc[df_tcp["src_ip_addr"].isin(['10.0.0.1'])]
    df_h2_tcp = df_tcp.loc[df_tcp["src_ip_addr"].isin(['10.0.0.2'])]
    df_h1_udp = df_udp.loc[df_udp["src_ip_addr"].isin(['10.0.0.1'])]
    df_h2_udp = df_udp.loc[df_udp["src_ip_addr"].isin(['10.0.0.2'])]
    fig.append_trace({
        'x': df_h1_tcp["src_ip_addr"],
        'y': df_h1_tcp["# of bytes"],
        'type': 'bar',
        'name': 'host1 TCP'
    }, 1, 1)
    fig.append_trace({
        'x': df_h2_tcp["src_ip_addr"],
        'y': df_h2_tcp["# of bytes"],
        'type': 'bar',
        'name': 'host2 TCP'
    }, 1, 2)
    fig.append_trace({
        'x': df_h1_udp["src_ip_addr"],
        'y': df_h1_udp["# of bytes"],
        'type': 'bar',
        'name': 'host1 UDP'
    }, 2, 1)
    fig.append_trace({
        'x': df_h2_udp["src_ip_addr"],
        'y': df_h2_udp["# of bytes"],
        'type': 'bar',
        'name': 'host2 UDP'
    }, 2, 2)
    return fig
if __name__ == '__main__':
    app.run(debug=True)
