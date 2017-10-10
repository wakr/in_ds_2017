import geopandas as gpd
import matplotlib.pyplot as plt

world = gpd.read_file('../data/citydata/geo_export.shp')

#cities.plot(marker='*', color='green', markersize=5)
#cities = cities.to_crs(world.crs)

base = world.plot(color='white', edgecolor='black')
#cities.plot(ax=base, marker='o', color='red', markersize=5)

plt.show()