
from flask import Flask, render_template
import json

# pip install plotly==3.9.0
# pip install plotly
import plotly
import plotly.plotly as py
import plotly.graph_objs as go
import numpy as np

app = Flask(__name__)
 
@app.route('/')
def line():
    # count = 500
    # xScale = np.linspace(0, 100, count)
    # yScale = np.random.randn(count)
    xScale = [0,1,2,3,4,5,6,7,8,9,10]
    yScale = [0,1,2,3,4,5,6,7,8,9,10]

    # Create a trace
    trace = go.Scatter(
        x = xScale,
        y = yScale
    )
 
    data = [trace]
    graphJSON = json.dumps(data, cls = plotly.utils.PlotlyJSONEncoder)
    return render_template('plotly390_chart.html', graphJSON = graphJSON)

if __name__ == '__main__':
    app.run(debug=True)