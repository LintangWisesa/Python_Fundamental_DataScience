# pip install folium
import folium

# map
m = folium.Map(
    location = [-6.1753924, 106.8271528],
    tiles='OpenStreetMap',  # 'Stamen Terrain', 'Stamen Toner', 'Mapbox Bright', 'Mapbox Control Room'
    zoom_start = 17
)

print(m)
m.save('0.html')