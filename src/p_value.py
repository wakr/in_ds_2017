import pandas as pd
import numpy as np
from scipy.stats.stats import pearsonr

df = pd.read_csv("../assets/schooldata.csv")

df = df.groupby(['ZIP Code']).mean()

print(list(df.columns.values))

crimedf = pd.read_csv('../data/crimes_zipcode_added.csv')

asd = crimedf.groupby(['Zipcode']).size().reset_index(name='counts')

a = {}
b = {}

for index, row in asd.iterrows():
    a[row['Zipcode']] = row['counts']

for index, row in df.iterrows():
    b[index] = row['Safety Score']

p_a = []
p_b = []
b_keys = b.keys()

for i in a.keys():
    if i in b.keys():
        p_a.append(a[i])
        p_b.append(b[i])

print(pearsonr(p_a, p_b))

index = 0
for i in p_a:
    print(str(i) + " " + str(p_b[index]))
    index += 1

