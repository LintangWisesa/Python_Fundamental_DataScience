import plotly.graph_objects as go

fig = go.Figure(
    data=[go.Bar(x=[1, 2, 3], y=[1, 3, 2])],
    layout_title_text= "A Figure Displayed with fig.show()"
)

fig.show()

# it will run automatically at (for example) http://127.0.0.1:51084/