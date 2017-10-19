# -*- coding: utf-8 -*-
%matplotlib inline
import pandas as pd
from matplotlib.pylab import rcParams
rcParams['figure.figsize'] = 5, 2
#%% Get identifier for months

def parse_date_month(d):
    parsed = d.split(" ")[0].split("/")
    return parsed[2]+ "-" + parsed[0]

#%%

df = pd.read_csv("data/crimes_in_polygon.csv")
df = df.query("Year < 2017")[["ID", "Date", "Year", "Zip"]]
df["Month"] = df["Date"].apply(parse_date_month)
df["Month"] = pd.to_datetime(df["Month"])
#%%

df_by_year = df.groupby("Year").count().ID
df_by_year.plot(title="Crime rate in Chicago from 2010-2017", marker='o')
#%%
df_by_month = df.groupby("Month").count().ID
df_by_month.plot(title="Crime rate per month in Chicago")
