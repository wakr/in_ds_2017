# -*- coding: utf-8 -*-

%matplotlib inline
import pandas as pd
import matplotlib as mpl
import json
from bokeh.io import show, output_notebook, output_file
from bokeh.models import (
    GeoJSONDataSource,
    HoverTool,
    LinearColorMapper,
    ColumnDataSource,
    LogColorMapper
)
from bokeh.plotting import figure
from bokeh.palettes import Viridis6 as palette

mpl.rcParams['figure.figsize'] = (16,8)
mpl.style.use('ggplot')
palette.reverse()
color_mapper = LogColorMapper(palette=palette)
#%%

df = pd.read_csv("data/crimes.csv")

#%%

df["Primary Type"] = df["Primary Type"].astype('category')
df["Primary Type"].unique()

#%%

df["Beat"] = df["Beat"].astype('category')

#%%

beat_crime_distr = df.groupby("Beat").size()
beat_crime_distr.index = beat_crime_distr.index.astype("str")
total_crimes = beat_crime_distr.sum() 
beat_crime_as_percent = beat_crime_distr\
                            .div(total_crimes)\
                            .multiply(1000)\
                            .round(2)\
                            .to_dict()
#%%

with open(r'map/police_beats/police_beats.geojson', 'r') as f:
    geojson = json.loads(f.read())
    # append aggregated crime counts
    for i in range(len(geojson["features"])):
        di = geojson["features"][i]
        di_id = di["properties"]["beat_num"]
        if di_id in beat_crime_as_percent:
            di["properties"]["crime_rate"] = beat_crime_as_percent[di_id]
        else:
            di["properties"]["crime_rate"] = None
    geojson = json.dumps(geojson)
    geo_source = GeoJSONDataSource(geojson=geojson)
    
        
    

#%%

hover = HoverTool(tooltips=[
    ("beat_num", "@beat_num"),
    ("beat", "@beat"),
    ("crime_rate", "@crime_rate%%")
])

    
p = figure(title="Chicago beats", 
           tools=[hover, "pan,wheel_zoom,box_zoom,reset"], 
           x_axis_location=None, 
           y_axis_location=None,
           plot_width=1000,
           plot_height=1000)

p.grid.grid_line_color = None

p.patches('xs', 'ys', 
          line_color='black', 
          fill_color={'field': 'crime_rate', 'transform': color_mapper},
          line_width=1, 
          source=geo_source)

#%%

show(p)