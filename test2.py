import numpy 
from mpl_toolkits.basemap import Basemap
import matplotlib.pyplot as plt

# Define locations of my vectors
lat = numpy.array([50.1,46.2,51.6,52.2,54.4])
lon = numpy.array([-3.3,-1.0,-5.2,-1.2,0.2])

# Define some east-west vectors to illustrate the problem
u = numpy.array([5,5,5,5,5])
v = numpy.array([0,0,0,0,0])

# Set up map projection
m = Basemap(llcrnrlon=-15.,llcrnrlat=46.,urcrnrlon=15.,urcrnrlat=59.,
            projection='lcc',lat_1=40.,lat_2=50.,lon_0=-50.,
            resolution ='l')

# Calculate positions of vectors on map projection 
x,y = m(lon,lat)

# Calculate the orientation of the vectors
x1, y1 = m(lon+u, lat+v)
u_map, v_map = x1-x, y1-y

# Rescale the magnitudes of the vectors...
mag_scale = numpy.hypot(u_map, v_map) / numpy.hypot(u, v)
u_map /= mag_scale
v_map /= mag_scale

# Draw barbs
m.barbs(x,y,u_map,v_map, length=7, color='red')

# Draw some grid lines for reference
parallels = numpy.arange(-80.,90,20.)
meridians = numpy.arange(0.,360.,20.)
m.drawparallels(parallels)
m.drawmeridians(meridians)
m.drawcoastlines(linewidth=0.5)

plt.show()