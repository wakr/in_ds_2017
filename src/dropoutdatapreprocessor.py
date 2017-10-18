import pandas as pd
import numpy as np

df = pd.read_csv("../assets/parempi.csv")

def convert_float_2014(x):
    if pd.isnull(x['2014']):
        return np.NaN
    return float(x['2014'].split(",")[0] + "." + x['2014'].split(",")[1])

def convert_float_2011(x):
    if pd.isnull(x['2011']):
        return np.NaN
    return float(x['2011'].split(",")[0] + "." + x['2011'].split(",")[1])

def convert_float_2012(x):
    if pd.isnull(x['2012']):
        return np.NaN
    return float(x['2012'].split(",")[0] + "." + x['2012'].split(",")[1])

def convert_float_2013(x):
    if pd.isnull(x['2013']):
        return np.NaN
    return float(x['2013'].split(",")[0] + "." + x['2013'].split(",")[1])

df['2011'] = df.apply(convert_float_2011, axis=1)
df['2012'] = df.apply(convert_float_2012, axis=1)
df['2013'] = df.apply(convert_float_2013, axis=1)
df['2014'] = df.apply(convert_float_2014, axis=1)

#df = df.groupby(df.columns, axis = 1).transform(lambda x: x.fillna(x.mean()))

df.drop(df.columns[[3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]], axis=1, inplace=True)

df = df.groupby(df.columns, axis = 1).transform(lambda x: x.fillna(x.mean()))

df.to_csv("dropouts_preprocessed.csv")

print(df.shape)