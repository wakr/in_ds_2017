# -*- coding: utf-8 -*-

import pandas as pd

#%% 

dfa = pd.read_csv('data/Chicago_Crimes_2008_to_2011.csv',
                  error_bad_lines=False)

dfb = pd.read_csv('data/Chicago_Crimes_2012_to_2017.csv',
                  error_bad_lines=False)

#%% Take only 2010 onwards

dfa = dfa.query("Year >= 2010")

#%% Drop Nan rows

dfa = dfa.dropna(axis=0, how='any')
dfb = dfb.dropna(axis=0, how='any')

#%% Combine

df = pd.concat([dfa, dfb])

#%%

df.to_csv("data/crimes.csv", index_label=False)