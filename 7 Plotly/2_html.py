# plotly 4.1.0
import plotly.graph_objects as go

fig = go.Figure(data=go.Bar(y=[2, 3, 1]))

fig.write_html(
    '2_html.html', 
    auto_open=True
)