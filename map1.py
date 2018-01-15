import folium  # module to convert python code to html/css/javascript
import csv

# Create map object with world map centered in Las Vegas
our_map = folium.Map(location=[36.174642, -115.091515], zoom_start=4)

# Create layers that can group several items which you can turn on and off simultaneously later on
fgv = folium.FeatureGroup(name='Volcanoes')
fgp = folium.FeatureGroup(name='Population')


# Set color for marker depending on elevation of a volcano
def get_color(elevation):
    if elevation < 1000:
        return 'green'
    elif 1000 < elevation < 3000:
        return 'orange'
    else:
        return 'red'


# Get names and coordinates of USA's volcanoes
csv_file = open('Volcanoes_USA.txt')
csv_object = csv.reader(csv_file)
csv_list = list(csv_object)
csv_list = csv_list[1:]  # We do not need headers of csv file in our list


# Create list with name, elevation, longitude and latitude of each volcano
volcanoes = [[x[2], float(x[5]), float(x[8]), float(x[9])] for x in csv_list]

# Add markers pointing to these volcanoes
for i in volcanoes:
    # parse_html in order to not to break javascript because of ' inside strings
    fgv.add_child(folium.Marker(location=[i[2], i[3]], popup=folium.Popup(i[0] + ', ' + str(i[1]) + ' m',
                                parse_html=True), icon=folium.Icon(color=(get_color(i[1])))))

#  Make new layer to single out countries by color depending on a population
fgp.add_child(folium.GeoJson(data=open('world.json', 'r', encoding='utf-8-sig').read(),
                             style_function=lambda x: {'fillColor': 'green' if x['properties']['POP2005'] < 10000000 else
                            'orange' if 10000000 <= x['properties']['POP2005'] < 20000000 else 'red'}))

our_map.add_child(fgv)
our_map.add_child(fgp)
our_map.add_child(folium.LayerControl())

# Create actual interactive map
our_map.save('Map1.html')

