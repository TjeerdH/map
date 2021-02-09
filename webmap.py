import folium
import pandas as pd

file = pd.read_csv("airports.csv", index_col=2)
data = file.drop("heliport")
data = data.drop("closed")
data = data.drop("medium_airport")
data = data.drop("large_airport")
lat = list(data["latitude_deg"])
lon = list(data["longitude_deg"])
name = list(data["name"])
elevation = list(data["elevation_ft"])

def color_function(name):
	if name == "Aero Club Salland":
		return "red"
	else:
		return "blue"

map = folium.Map(location=[52.46564496296631, 6.333438527047803], tiles='https://{s}.basemaps.cartocdn.com/light_all/{z}/{x}/{y}{r}.png', attr='"https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors &copy; <a href="https://carto.com/attributions">CARTO</a>')
#map.add_child(folium.Marker(location=[52.46564496296631, 6.333438527047803],popup="My home airport!", icon=folium.Icon(color="red")))
layer_control = folium.LayerControl()
airports = folium.FeatureGroup(name="Airports")

for lt, ln, n, e in zip(lat,lon, name, elevation):
	airports.add_child(folium.Marker(location=[lt, ln], popup=f"Name:{n}\n Elevation:{e} ft ", icon=folium.Icon(color=color_function(n))))

map.add_child(airports)
map.add_child(layer_control)


map.save("map.html")