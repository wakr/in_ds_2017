import pandas as pd
import numpy as np
from uszipcode import ZipcodeSearchEngine


search = ZipcodeSearchEngine()
df = pd.read_csv("../assets/schooldata.csv")

df = df.groupby(['ZIP Code']).mean()

#for index, row in df.iterrows():
 #   print(row)

#df.to_csv('preprocessed_schooldata.csv')

print(list(df.columns.values))

def add_zipcode(x):
    if pd.isnull(x['Latitude']) or pd.isnull(x['Longitude']):
        return np.NaN
    else:
        coords = [x['Latitude'], x['Longitude']]
        if coords[0] != coords[0] or coords[1] != coords[1]:
            return np.NaN
        res = search.by_coordinate(coords[0], coords[1], radius=30, returns=1)
        return res[0]['Zipcode']

df = pd.read_csv("../assets/schooldata.csv")
crimedf = pd.read_csv('../data/crimes.csv')

crimedf['Zipcode'] = crimedf.apply(add_zipcode, axis=1)

asd = crimedf.groupby(['Zipcode']).count()
crimedf.to_csv('crimes_zipcode_added.csv')

print(asd.shape)