import folium  # module to convert python code to html/css/javascript

# Create map object with world map centered in Las Vegas
our_map = folium.Map(location=[36.174642, -115.091515], zoom_start=4)

# Create layer that can group several items which you can turn on and off simultaneously later on
fg = folium.FeatureGroup(name='My Map')

# Add marker pointing to Las Vegas High Roller
fg.add_child(folium.Marker(location=[36.117941, -115.168246], popup='High Roller',
                           icon=folium.Icon(color='green')))

our_map.add_child(fg)

# Create actual interactive map
our_map.save('Map1.html')

