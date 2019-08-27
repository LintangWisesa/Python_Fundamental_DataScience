# pip install folium
import folium

peta = folium.Map(
    location = [-6.1753924, 106.8271528],
    tiles = 'OpenStreetMap',
    zoom_start = 15
)

# marker
folium.Marker(
    [-6.1763924, 106.8261528],
    popup = '<b>Spongebob</b><br><i>Jakarta</i>',
    tooltip = '<img width="100px" src="https://www.merchandisingplaza.us/42675/2/T-shirts-Sponge-Bob-SPONGEBOB-SQUAREPANTS-Big-Spotted-Face-Yellow-Graphic-Tee-Shirt-l.jpg"/>',
    icon = folium.Icon(color='orange', prefix='fa', icon='user')
).add_to(peta)

folium.Marker(
    [-6.1753929, 106.8271530],
    popup = '<b>Patrick</b><br><i>Jakarta</i>',
    tooltip = '<img width="100px" src="https://cdn.shopify.com/s/files/1/0150/0643/3380/products/Viacom_Spongebob_Delta9500_00048_Pink_RO_800x.jpg"/>',
    icon = folium.Icon(color='pink', prefix='fa', icon='user')
).add_to(peta)

peta.save('0.html')