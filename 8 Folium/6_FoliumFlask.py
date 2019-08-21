from flask import Flask
import folium

app = Flask(__name__)

@app.route('/')
def index():
    start_coords = (-6.1753924, 106.8271528)
    folium_map = folium.Map(
        location=start_coords, 
        zoom_start=17
    )
    return folium_map._repr_html_()

if __name__ == '__main__':
    app.run(debug=True)

# next:
# insert folium on html rendered by flask
# https://stackoverflow.com/questions/37379374/insert-the-folium-maps-into-the-jinja-template
