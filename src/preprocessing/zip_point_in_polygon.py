# -*- coding: utf-8 -*-

import pandas as pd

from shapely.geometry import Point
from shapely.geometry.polygon import Polygon

from bokeh.models import (
    GeoJSONDataSource,
    HoverTool,
    LinearColorMapper,
    ColumnDataSource
)

import json

#%%


df = pd.read_csv('data/crimes.csv')

#%%

with open(r'map/zip/zip_codes.geojson', 'r') as f:
    geojson = json.loads(f.read())
    

poly_zips = {}
for z in geojson["features"]:
    zip_code = z["properties"]["zip"]
    polygon = z["geometry"]["coordinates"][0][0]
    poly_zips[zip_code] = Polygon(polygon)
    
#%%    

def get_zip(point):
    lat, lon = point
    for z in poly_zips.keys():
        # notice flipped lat,lon
        if poly_zips[z].contains(Point(lon, lat)):
            return z
    return None

#%% testers, check from Google (lat, lon)
    
#60609    
pp = (41.80171934, -87.630703621)
# 60639
pp2 = (41.909839206, -87.735702897)
#%%

df["Zip"] = df['Location'].apply(lambda x: get_zip(eval(x)))


#%%
df = df.dropna(axis=0, how='any')

#%%
df.to_csv("data/crimes_in_polygon.csv", index_label=False)