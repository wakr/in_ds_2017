import geopandas as gpd
import matplotlib.pyplot as plt
import pandas as pd

world = gpd.read_file('../shape/zipit.geojson')
data = pd.read_csv('../data/Chicago_Crimes_2012_to_2017.csv')
print(list(data.columns.values))
crime_coordinates = []

for index, row in data.iterrows():
    coords = [row['X Coordinate'], row['Y Coordinate']]
    crime_coordinates.append(coords)


#boundaries = gpd.read_file('../shape/zip/geo_export.shp')

#cities.plot(marker='*', color='green', markersize=5)
#cities = cities.to_crs(world.crs)

base = world.plot(color='white', edgecolor='black')
#boundaries.plot(ax=base)

plt.show()