import folium

m = folium.Map(
    location=[-6.1753924, 106.8271528],
    tiles='Stamen Terrain',
    zoom_start=17
)

m.add_child(folium.LatLngPopup())

m