# Plotly express (included as the plotly.express module) is a 
# high-level data exploration API that produces graph object figures.

import plotly.express as px
iris = px.data.iris()
print(iris)

fig = px.scatter(
    iris, 
    x="sepal_width", 
    y="sepal_length", 
    color="species"
)

# If you print fig, you'll see that it's just a regular figure with data and layout
# print(fig)
fig.show()