# Folium to locate and display coordinates on a map
# Pandas to read file and use data from it
import pandas
import folium

# Reading file and storing its data in a object.
data = pandas.read_csv("Volcanoes_USA.txt")
map = folium.Map([38, -120], zoom_start = 6, tiles = "Mapbox Bright")
# map = folium.Map([38, -120], zoom_start = 6)

lat = list(data["LAT"])
lon = list(data["LON"])
elev = list(data["ELEV"])
name = list(data["NAME"])

# Function to produce color depending upon the elevation
# @param elevation: the elevation of a Volcano
def color_producer(elevation):
    if elevation < 1000:
        return 'green'
    elif 1000 <= elevation < 3000:
        return 'orange'
    else:
        return 'red'


fgv = folium.FeatureGroup(name = "Volcanoes")

for lt, lo, el, nm in zip(lat, lon, elev, name):
    popup = folium.Popup(str(el) + " m, " + nm, parse_html=True)
    # fg.add_child(folium.Marker(location = [lt, lo], popup = popup, icon = folium.Icon(color = color_producer(el))))
    fgv.add_child(folium.CircleMarker(location = [lt, lo], popup = popup, color = 'grey', fill_color = color_producer(el), fill = True, radius = 5, fill_opacity = 0.8))

fgp = folium.FeatureGroup(name = "Population")

fgp.add_child(folium.GeoJson(open("world.json", encoding = "utf-8-sig").read(),
style_function = lambda x: {'fillColor' : 'green' if x['properties']['POP2005'] < 10_000_000
else 'blue' if 10_000_000 <= x['properties']['POP2005'] < 20_000_000
else 'red' if 20_000_000 <= x['properties']['POP2005'] < 50_000_000 else 'darkbrown'}))


map.add_child(fgv)
map.add_child(fgp)

# Always add LayerControl after adding child otherwise it won't work.
map.add_child(folium.LayerControl())

map.save("map_world.html")
