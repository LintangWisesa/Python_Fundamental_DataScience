# pip install plotly
import plotly.graph_objects as go

x = [1,2,3,4,5]
y = [5,4,3,4,2]
fig = go.Figure(
    data = [go.Scatter(
        x=x, y=y, mode='lines+markers',
        marker = {'color': ['red'] * 5},
        line = {'color': 'yellow'}
    )],
    layout_title_text = 'Ini plot pakai plotly'
)
fig.write_html('plot1.html', auto_open=True)
fig.show()