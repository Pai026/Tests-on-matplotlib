from mpl_toolkits.basemap import Basemap 
import matplotlib.pyplot as plt
map = Basemap()
map.drawmapboundary(fill_color='aqua')
map.fillcontinents(color='coral',lake_color='aqua')
map.drawcoastlines()
plt.show()
plt.savefig('test.png')