# -*- coding: utf-8 -*-

import pandas as pd
import pandas as pd
import matplotlib as mpl
import json
from bokeh.io import output_notebook
from bokeh.models import (
    GeoJSONDataSource,
    HoverTool,
    LinearColorMapper,
    ColumnDataSource,
    LogColorMapper,
    LogTicker,
    ColorBar
)
from bokeh.plotting import figure, show
from bokeh.layouts import row
from bokeh.palettes import Viridis6 as palette
from bokeh.palettes import RdYlGn11 as palette2

#%%

df = pd.read_csv("assets/joined_grouped_schooldata.csv")
df_s = pd.Series(df['years_average'].values, index=df['ZIP Code'])
#%%

color_mapper = LogColorMapper(palette=palette2,
                                 low=df_s.min(),
                                 high=df_s.max())

with open(r'map/zip/zip_codes.geojson', 'r') as f:
    geojson = json.loads(f.read())
    # append aggregated crime counts
    for i in range(len(geojson["features"])):
        di = geojson["features"][i]
        di_id = int(di["properties"]["zip"])
        if di_id in df_s.index:
            di["properties"]["drop_rate"] = df_s[di_id]
        else:
            di["properties"]["drop_rate"] = "None"
    geojson = json.dumps(geojson)
    geo_source = GeoJSONDataSource(geojson=geojson)
 
hover = HoverTool(tooltips=[
    ("zip", "@zip"),
    ("drop_rate", "@drop_rate%")
])
    
p1 = figure(title="Chicago school dropout per ZIP", 
           tools=[hover, "pan,wheel_zoom,box_zoom,reset"], 
           x_axis_location=None, 
           y_axis_location=None,
           toolbar_location=None)

p1.grid.grid_line_color = None

p1.patches('xs', 'ys', 
          line_color='black', 
          fill_color={'field': 'drop_rate', 'transform': color_mapper},
          line_width=1, 
          source=geo_source)


show(p1)
#%%