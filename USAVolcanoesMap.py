#!/usr/bin/python

#=========================================================================#
# Author      : Ankit Sharma                                              #
# Script      : USAVolcanoesMap.py                                        #
# Py Versions : 3.5                                                       #
# Required    : folium, pandas                                            #
# Execute     : python USAVolcanoesMap.py                                 #
#=========================================================================#

import folium
import pandas

# Load Volcanoes_USA.txt csv file using pandas.
data = pandas.read_csv('Volcanoes_USA.txt')
# Extract the LAT and LON fields from csv file using data DF
lat = list(data["LAT"])
lon = list(data["LON"])
ele = list(data["ELEV"])

def mcolor_producer(elevation):
  if elevation < 1000:
    return 'green'

  elif 1000 <= elevation <= 3000:
          return 'orange'

  else:
    return 'red'

# Create a Basic Map with locationa and zoom value.
mymap = folium.Map(location=[38.58, -99.09], zoom_start=6)

# Create FeatureGroup.
fgv = folium.FeatureGroup(name="Volcanoes")

# Loop to update the marker using coordinates.
for la, lo, el in zip(lat, lon, ele):
  fgv.add_child(folium.CircleMarker(location=[la, lo], radius=6,
  popup=str(el)+" m",
  fill=True,
  fill_color=mcolor_producer(el),
  color='grey',
  fill_opacity=0.7))

fgp = folium.FeatureGroup(name="Population")

fgp.add_child(folium.GeoJson(data=open('world.json', 'r', encoding='utf-8-sig').read(),
style_function=lambda x: {'fillColor':'yellow' if x['properties']['POP2005'] < 10000000 else 'orange' if 10000000 <= x['properties']['POP2005'] < 20000000 else 'red'}))

mymap.add_child(fgp)
mymap.add_child(fgv)

mymap.add_child(folium.LayerControl())

mymap.save("Volcanoes_USA.html")
