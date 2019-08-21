from flask import Flask, render_template
import folium

app = Flask(__name__)

@app.route('/')
def index():
    start_coords = (-6.1753924, 106.8271528)
    folium_map = folium.Map(
        location=start_coords, 
        zoom_start=17
    )
    folium_map.save('templates/7_map.html')
    return render_template('7_index.html')

@app.route('/map')
def map():
    return render_template('7_map.html')

if __name__ == '__main__':
    app.run(debug=True)