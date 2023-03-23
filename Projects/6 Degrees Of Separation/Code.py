# -*- coding: utf-8 -*-
"""
Created on Thu Dec 10 14:30:59 2020

@author: lockd

We have facebook data in file facebook_combined.txt.gz. 
This is in edge list representation. Here anonymous people 
are taken as nodes and edge between any two nodes 
represents friendship between them. Now, we have to prove
the theory of Six Degrees of Separation.

We will create graph by reading  all the nodes and edges 
from edgelist using in-built function nx.read_edgelist()

We have to find the length of shortest path(no. of edges 
between the shortest path) between each pair of nodes. For
that we will create a list 'N' containing all nodes of 
graph and wll also create an empty list 'SPLL' for storing the 
length

Then, run a loop to find length l of shortest path between
each pair of node and append this l to SPLL for each 
pair of node

Find minimum, maximum and average value of SPLL. We will 
come to know that average value of SPLL is 6 i.e. on avg.
length of shortest path between any pair of node is 6
Hence, proving Six Degree Of Separation

"""


import networkx as nx 
import numpy #For avg

#Creates graph G by reading all the nodes and edges from edgelist
G = nx.read_edgelist('facebook_combined.txt.gz')

#nx.draw(G) #Draws G. However, we don't need to draw graph

N = list(G.nodes()) #G.nodes() returns nodes of G and we are converting that into list


SPLL = []

for a in N:
    for b in N:
        if a!=b: #Because We don't want to find length between two same nodes i.e. a and a
            l = nx.shortest_path_length(G, a, b) #In built function to find shortest path between a and b node of graph G
            print('Shortest Path between ',a,' and ',b,' is of length ',l)
            SPLL.append(l)
        
            
min_SPL = min(SPLL) #In built function to find min
max_SPL = max(SPLL) #In built function to find max   
avg_SPL = numpy.average(SPLL)     

print('Minimum Shortest Path Length = ', min_SPL)       
print('Maximum Shortest Path Length = ', max_SPL)
print('Average Shortest Path Length = ', avg_SPL)
