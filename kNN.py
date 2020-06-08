#K-Nearest Neighbor Assignment
#submitted March 2018
#last edited 6/8/2020
#
#I don't recall what the data was supposed to represent,
# but I do know it was to practice K-NN. 
#
# Last edited so that it runs smoothly with Python 3

from __future__ import division
import numpy as np
import matplotlib as mplot
import matplotlib.pyplot as plt
import math
import time

#distance formula
def dist(a, b):
    return math.sqrt(math.pow(a[0]-b[0],2)+math.pow(a[1]-b[1],2))



#start timer
start = time.time()

#create grid instances
border_grid = []
data_grid = []
new_grid = []

#read in map outline points
mpdata = open("us_outline.csv", 'r')
mpdata = mpdata.read()
mpdata = mpdata.split('\n')

#append map data to border grid
for line in mpdata:
    line = line.split(", ")
    x = np.float32(line[0])
    y = np.float32(line[1])
    border_grid.append([x,y])

#read in the reference data
data = open("data.csv", 'r')
data = data.read()
data = data.split('\n')

#append reference data to the reference data grid
for line in data:
    line = line.split(",")
    x = np.float32(line[0])
    y = np.float32(line[1])
    z = np.float32(line[2])
    data_grid.append([x,y,z])

#sort grid and copy to the new grid
data_grid = sorted(data_grid)

#get k from user and check for validity
k = int(input("Select a positive integer value for k\n"))
if (k<1):
    print ("Invalid k value!!!")
else:
    k = int(k)

#kNN
test_node = []
dist_list = []
col = 1;

for x in range(195):
    for y in range(120):
        test_node = [x,y]
        avg = 0.0
        for v in data_grid:#gets distance b/w node and all data points
            dist_list.append([v,dist(v,test_node)])
        dist_list = sorted(dist_list, key=lambda val:val[col])#sorts by distance
        dist_list = dist_list[0:k]
        for row in dist_list:
            avg += row[0][2]
        avg = avg/k
        new_grid.append([x,y,avg])
        dist_list[:] = []


#sort the new grid and create lists for x,y, and v
new_grid = sorted(new_grid)
x=[]
y=[]
v=[]

#append xyv lists with new grid data
for row in new_grid:
    x.append(row[0])
    y.append(row[1])
    v.append(row[2])

#append a&b lists with border grid values
a=[]
b=[]
for r in border_grid:
    a.append(r[0])
    b.append(r[1])

#plot data, end timer, print time and show plot
plt.scatter(x, y, c=v, cmap="viridis")
plt.plot(a, b, c="black")
plt.show()
end = time.time()
total_time = (end-start)*1000000
print ("Execution time: ", total_time,"us")
