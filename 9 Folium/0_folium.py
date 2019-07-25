# pip install folium
import folium

m = folium.Map(
    location = [-6.1753924, 106.8271528],
    zoom_start = 17
)

tooltip = 'Klik sini!'
folium.Marker(
    [-6.1753924, 106.8271528], 
    popup = '<b>Monumen Nasional</b><br><i>Jakarta</i>', 
    tooltip = tooltip,
    icon = folium.Icon(color='red', icon='info-sign')
).add_to(m)

folium.CircleMarker(
    location = [-6.1753924, 106.8271528],
    radius = 130,
    popup = '<i>Taman Monas</i>',
    color = '#3186cc',
    fill = True,
    fill_color = '#FFFF00',
).add_to(m)

print(m)
m.save('0.html')