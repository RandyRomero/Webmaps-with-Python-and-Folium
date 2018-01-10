import folium  # module to convert python code to html/css/javascript
import csv

# Create map object with world map centered in Las Vegas
our_map = folium.Map(location=[36.174642, -115.091515], zoom_start=4)

# Create layer that can group several items which you can turn on and off simultaneously later on
fg = folium.FeatureGroup(name='My Map')


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
    fg.add_child(folium.CircleMarker(location=[i[2], i[3]], popup=folium.Popup(i[0] + ', ' + str(i[1]) + ' m',
                                     parse_html=True), color='gray', fill_color=get_color(i[1]), fill_opacity=1, fill=True))

our_map.add_child(fg)

# Create actual interactive map
our_map.save('Map1.html')

