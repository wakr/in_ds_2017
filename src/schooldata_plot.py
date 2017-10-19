import pandas as pd
import numpy as np

import matplotlib.pyplot as plt


x = np.array([2011,2012,2013,2014, 2015, 2016])
df = pd.read_csv("../assets/joined_grouped_schooldata.csv")
df = df[["2011", "2012", "2013", "2014", "2015", "2016"]]

values = [df["2011"].mean()*0.01, df["2012"].mean()*0.01, df["2013"].mean()*0.01, df["2014"].mean()*0.01, df["2015"].mean()*0.01, df["2016"].mean()*0.01]

#my_xticks = ['2011','2012','2013','2014', '2015', '2016']
#plt.xticks(values, my_xticks)
plt.ylabel('Dropout rate', fontsize=11)

plt.plot(x, values)

plt.show()
print(values)