# -*- coding: utf-8 -*-

import pandas as pd
from bokeh.io import show, output_notebook, output_file
from bokeh.models import (
    GeoJSONDataSource,
    HoverTool,
    LinearColorMapper,
    ColumnDataSource
)
from bokeh.plotting import figure
from bokeh.palettes import Viridis6
#%%

limit = 100000
df = pd.read_csv("data/crimes.csv", nrows=limit)
psource = ColumnDataSource(df)


#%%

with open(r'map/zip/zip_codes.geojson', 'r') as f:
    geo_source = GeoJSONDataSource(geojson=f.read())

hover = HoverTool(tooltips=[
    ("index", "$index"),
    ("(x,y)", "($x, $y)"),
    ("zip", "@zip"),
])

p = figure(title="Chicago", tools=[hover, "pan,wheel_zoom,box_zoom,reset"], x_axis_location=None, y_axis_location=None
           , plot_width=1000, plot_height=1000)

p.grid.grid_line_color = None

p.patches('xs', 'ys', fill_alpha=0.3, 
          line_color='white', line_width=0.5, source=geo_source)

p.cross('Longitude', 'Latitude', source=psource, color='red', size=0.1)
#%%
show(p)

#%%




