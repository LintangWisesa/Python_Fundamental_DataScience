# pip install folium
import folium

# map
m = folium.Map(
    location = [-6.1753924, 106.8271528],
    tiles='OpenStreetMap',  # 'Stamen Terrain', 'Stamen Toner', 'Mapbox Bright', 'Mapbox Control Room'
    zoom_start = 17
)

# marker
tooltip = 'Klik sini!'
folium.Marker(
    [-6.1753924, 106.8271528], 
    popup = '<b>Monumen Nasional</b><br><i>Jakarta</i>', 
    tooltip = tooltip,
    icon = folium.Icon(color='red', icon='info-sign')   # icon='cloud'
).add_to(m)

print(m)
m.save('0.html')