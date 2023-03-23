# -*- coding: utf-8 -*-
"""
Created on Fri Nov 27 11:10:03 2020

@author: lockd

GPS Route Tracker
Track the vehicle which has GPS tracker
"""


import csv #To use csv file
from gmplot import gmplot #To use map

gmap = gmplot.GoogleMapPlotter(32.73893451605284, 74.87393994911304, 18)

with open('D:/My Python Projects/Week 7/GPS ROUTE TRACKER/Route.csv','r') as f: #We created file because we don't have the live coordinates. In reality, the GPS tracker gives the live coordinates of vehicle 
    
    reader = csv.reader(f)
    k = 0 #K is used to plot the starting location with diferent colour
    
    for row in reader:
        lat = float(row[0])
        lon = float(row[1])
        
        if(k==0):
            gmap.marker(lat,lon,'yellow')   #To mark location
            k = 1
        else:
            gmap.marker(lat,lon,'blue')
gmap.marker(lat,lon,'red')      

gmap.draw('D:/My Python Projects/Week 7/GPS ROUTE TRACKER/Route On Map.html') #It stores the plotted graph in the html file. 
#We don't have to create the html file by ourselves as we did in the case of csv file. We just have to write the desired name and path where we want to store that file. Even if wo don't write the path, then the file will get stored at location where program is stored.     
