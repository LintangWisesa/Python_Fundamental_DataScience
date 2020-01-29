import plotly.graph_objects as go

plot = go.Scatter(
    x = [0,1,2,3,4,5,6,7,8,9],
    y = [1,0,2,1,4,3,6,5,5,7]
)

fig = go.Figure(
    data = [plot],
    layout_title_text = "Tes plotly"
)

fig.show()
