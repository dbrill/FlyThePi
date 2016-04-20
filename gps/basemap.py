from mpl_toolkits.basemap import Basemap
import matplotlib.pyplot as plt
import numpy as np
import csv
import os

#llcrnr = lower left corner
#urcrnr = upper right corner

#corner coords of CU campus area
llcrnrlon = -105.2833
urcrnrlon = -105.2434

llcrnrlat = 39.9893
urcrnrlat = 40.0135

my_map = Basemap(llcrnrlon= llcrnrlon, urcrnrlat= urcrnrlat, urcrnrlon= urcrnrlon, llcrnrlat= llcrnrlat,
        resolution='h', projection='merc')

lats = []
lons = []
with open("collect.csv", "rb") as f:
	reader = csv.reader(f,delimiter=",")
	for row in reader:
		lats.append(row[0])
		lons.append(row[1])



#boulders coords:
#lat = 40.0100
#lon = -105.2705

RGB = (0.0,0.0,0.0)
#skips the first row to take into account the header strings
for i in range(1,len(lats)):
	x,y = my_map(float(lons[i]),float(lats[i]))
	my_map.plot(x,y,marker="o",color=RGB)
	RGB = ((RGB[0] +.05)%1,(RGB[1] +.05)%1,(RGB[2] +.05)%1)  #messing around with colors of points

#to add text to the map at coords x,y:
#plt.text(x,y, "Boulder", fontsize=12,fontweight="bold", ha="center", va="bottom")

#background.png image is from openstreetmap with corner coords from above
im = plt.imread('background.png')
my_map.imshow(im, interpolation='lanczos', origin='upper')

plt.title("Where is our Pi?")

#remove old image
# if os.path.isfile("map.png"):
# 	os.remove("map.png")
#save new image 
plt.savefig("map.png")


