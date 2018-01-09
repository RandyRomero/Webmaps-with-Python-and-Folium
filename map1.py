import folium  # module to convert python code to html/css/javascript
import csv

# Create map object with world map centered in Las Vegas
our_map = folium.Map(location=[36.174642, -115.091515], zoom_start=4)

# Create layer that can group several items which you can turn on and off simultaneously later on
fg = folium.FeatureGroup(name='My Map')

# TODO Add volcanoes as markers from Volcanoes.txt
csv_file = open('Volcanoes_USA.txt')
csv_object = csv.reader(csv_file)
csv_list = list(csv_object)
csv_list = csv_list[1:]
# Create list with name, longitude and latitude of each volcano
volcanoes = [[x[2], float(x[8]), float(x[9])] for x in csv_list]

# Add markers pointing to USA Volcanoes
for i in volcanoes:
    i[0] = i[0].replace('\'', '') if '\'' in i[0] else i[0]  # Strip ' if occurs in string else break javascript
    fg.add_child(folium.Marker(location=[i[1], i[2]], popup=i[0], icon=folium.Icon(color='green')))

our_map.add_child(fg)

# Create actual interactive map
our_map.save('Map1.html')

