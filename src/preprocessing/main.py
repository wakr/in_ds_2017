# -*- coding: utf-8 -*-

import pandas as pd

#%% 

dfa = pd.read_csv('data/Crimes_-_2001_to_present.csv',
                  error_bad_lines=False)

#%% Take only 2010 onwards

dfa = dfa.query("Year >= 2010 and Year < 2017")

#%% Drop Nan rows

dfa = dfa.dropna(axis=0, how='any')

#%% Combine

df = pd.concat([dfa])

#%%

df.to_csv("data/crimes.csv", index_label=False)