# -*- coding: utf-8 -*-

%matplotlib inline
import pandas as pd
import matplotlib as mpl
import json
from bokeh.io import output_notebook
from bokeh.models import (
    GeoJSONDataSource,
    HoverTool,
    LinearColorMapper,
    ColumnDataSource,
    LogColorMapper
)
from bokeh.plotting import figure, show
from bokeh.palettes import Viridis6 as palette
from bokeh.palettes import RdYlGn11

mpl.rcParams['figure.figsize'] = (8,8)
mpl.style.use('ggplot')
palette.reverse()
color_mapper = LogColorMapper(palette=palette)
output_notebook()
#%%

df = pd.read_csv("data/crimes_with_zip.csv")

#%%

df["Zipcode"] = df["Zipcode"].astype('category')

#%%

crimes_by_zip = df.groupby("Zipcode").size()
crimes_by_zip.index = crimes_by_zip.index.astype("str")
total_crimes = crimes_by_zip.sum() 
crimes_by_zip = crimes_by_zip\
                            .div(total_crimes)\
                            .multiply(100)\
                            .round(2)\
                            .to_dict()

#%% 

with open(r'map/zip/zip_codes.geojson', 'r') as f:
    geojson = json.loads(f.read())
    # append aggregated crime counts
    for i in range(len(geojson["features"])):
        di = geojson["features"][i]
        di_id = di["properties"]["zip"]
        if di_id in crimes_by_zip:
            di["properties"]["crime_rate"] = crimes_by_zip[di_id]
        else:
            di["properties"]["crime_rate"] = None
    geojson = json.dumps(geojson)
    geo_source = GeoJSONDataSource(geojson=geojson)
    
    
#%%

hover = HoverTool(tooltips=[
    ("zip", "@zip"),
    ("crime_rate", "@crime_rate")
])

    
p = figure(title="Chicago crimes per ZIP", 
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

#%%

school_df = pd.read_csv("assets/schooldata.csv")\
                .groupby("ZIP Code")\
                .mean()

school_df.rename(columns={'Rate of Misconducts (per 100 students) ': 'Misconducts'}, inplace=True)

ss_series = school_df["Safety Score"]
mis_series = school_df["Misconducts"]

#%%

color_mapper = LinearColorMapper(palette=RdYlGn11, low=ss_series.min(), high=ss_series.max())

with open(r'map/zip/zip_codes.geojson', 'r') as f:
    geojson = json.loads(f.read())
    for i in range(len(geojson["features"])):
        di = geojson["features"][i]
        di_id = di["properties"]["zip"]
        if di_id in crimes_by_zip:
            di["properties"]["safety_score"] = ss_series.get(int(di_id))
        else:
            di["properties"]["safety_score"] = None
    geojson = json.dumps(geojson)
    geo_source = GeoJSONDataSource(geojson=geojson)
    

hover = HoverTool(tooltips=[
    ("zip", "@zip"),
    ("safety_score", "@safety_score")
])

    
p = figure(title="Chicago school safety per ZIP", 
           tools=[hover, "pan,wheel_zoom,box_zoom,reset"], 
           x_axis_location=None, 
           y_axis_location=None)

p.grid.grid_line_color = None

p.patches('xs', 'ys', 
          line_color='black', 
          fill_color={'field': 'safety_score', 'transform': color_mapper},
          line_width=1, 
          source=geo_source)



