import geopandas as gpd
import matplotlib.pyplot as plt

world = gpd.read_file('../data/zip/geo_export.shp')
boundaries = gpd.read_file('../data/zip/geo_export.shp')

#cities.plot(marker='*', color='green', markersize=5)
#cities = cities.to_crs(world.crs)

base = world.plot(color='white', edgecolor='black')
boundaries.plot(ax=base)

plt.show()