import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv('../data/crimes_in_polygon.csv')

#df = df.groupby(['Primary Type']).mean()

unique_types = df['Primary Type'].unique()
dict = {}
df = df.rename(columns={'Primary Type': 'primary_type'})
lists = []

for i in unique_types:
    print(i)
    list = []
    list.append(df[(df.Year == 2010) | (df.primary_type == i)].shape[0])
    list.append(df[(df.Year == 2011) | (df.primary_type == i)].shape[0])
    list.append(df[(df.Year == 2012) | (df.primary_type == i)].shape[0])
    list.append(df[(df.Year == 2013) | (df.primary_type == i)].shape[0])
    list.append(df[(df.Year == 2014) | (df.primary_type == i)].shape[0])
    list.append(df[(df.Year == 2015) | (df.primary_type == i)].shape[0])
    list.append(df[(df.Year == 2016) | (df.primary_type == i)].shape[0])
    dict[i] = list
    lists.append(list)
    plt.plot(list)

plt.show()
print(dict)