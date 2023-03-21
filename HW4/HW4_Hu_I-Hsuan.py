"""
This script aims to solve networl flow porblem
@author: Hu, I-Hsuan
"""
import networkx
import matplotlib.pyplot as plt
import csv
import collections
import numpy

G = networkx.DiGraph()
#reading the nodes
supplynode = collections.defaultdict(dict)
demandnode = collections.defaultdict(dict)
with open (input('Input the node ')) as csvfile1:
    csvreader1 = csv.reader(csvfile1, delimiter = ',')
    for row in csvreader1:
        if row[2] == 'd':
            demandnode[row[0]] = int(row[1])
            G.add_node(row[0])
        if row[2] == 's':
            supplynode[row[0]] = int(row[1])        
            G.add_node(row[0])
#reading the links between nodes           
linklist = collections.defaultdict(dict)
capacity = collections.defaultdict(dict)
with open(input('Input the link ')) as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ',') 
    for row in csvreader:
        linklist[(row[0],row[1])] = int(row[2])
        if float(row[2]) != 0:
            capacity[(row[0],row[1])] = float(row[2])
#reading the nodes position
position = collections.defaultdict(tuple)
demaposi = collections.defaultdict(tuple)
with open(input('Input the location ')) as csvfile2:
    csvreader2 = csv.reader(csvfile2, delimiter = ',')
    for row in csvreader2:
        position[row[0]] = (float(row[1]),float(row[2]))
        if row[0] in demandnode.keys():
            demaposi[row[0]] = numpy.array([float(row[1]), float(row[2])])
#giving supply and demand nodes different colors      
colormap = []
for node in G:
    if int(node) < len(demandnode):
        colormap.append('blue')       
    else:
        colormap.append('green')
# add links between nodes
G.add_edges_from(linklist.keys())
# give a larger graph
plt.figure(3,figsize=(12,12)) 
# change the shape and the color of the node 
networkx.draw_networkx_nodes(G,demaposi,nodelist=demandnode.keys(),node_shape='s')
networkx.draw_networkx(G,position, node_color= colormap, with_labels=True)
plt.show()
# find the Degree centrality, Closeness centrality, and Betweenness centrality
d = networkx.degree_centrality(G)
degreeCent = {i:j for i, j in sorted(d.items(), key= lambda i: i[1], reverse= True)}
print('Degree centrality:',degreeCent)
c = networkx.closeness_centrality(G)
closenessCent = {i: j for i, j in sorted(c.items(), key= lambda i: i[1], reverse= True)}
print('Closeness centrality:', closenessCent)
b = networkx.betweenness_centrality(G)
betweennessCent = {i: j for i, j in sorted(b.items(), key= lambda i: i[1], reverse= True)}
print('Betweenness Centrality:', betweennessCent)


from gurobipy import *
dnode, dvalue = multidict(demandnode)
snode, svalue = multidict(supplynode)
link, capa = multidict(capacity)
model = Model ("minimum cost flow problem")

model.setParam('OutputFlag', False)

X = model.addVars(link, vtype = GRB.INTEGER, lb = 0, ub = GRB.INFINITY, name = 'x')
D = model.addVars(dnode, vtype = GRB.CONTINUOUS, lb = 0, ub = GRB.INFINITY, name = 'd')
# Supply constraints
for i in snode:
    model.addConstr(quicksum(X[i,j] for i, j in link.select(i,'*')) == supplynode[i])
# Demand constraints
for j in dnode:
    model.addConstr(quicksum(X[i,j] for i, j in link.select('*', j)) == D[j])

# link capacity constraints: maximum capacity
for j in dnode:
    model.addConstr (D[j] <= demandnode[j])  
    
# Define the objective function
Z = quicksum(demandnode[j] - D[j] for j in dnode)/997
model.setObjective(Z, GRB.MINIMIZE)
model.optimize()
if model.status == GRB.OPTIMAL:
    for i, j in link:
        if X[i,j].X != 0:    
            print('From', i, 'to', j, 'is', int(X[i,j].X))


'''
remove 5 node based on degree centrality
'''


removenode = ['6','9','4','5','8']
G = networkx.DiGraph()
supplynode = collections.defaultdict(dict)
demandnode = collections.defaultdict(dict)
with open (input('Input the node ')) as csvfile1:
    csvreader1 = csv.reader(csvfile1, delimiter = ',')
    for row in csvreader1:
        if row[0] in removenode:
            continue
        if row[2] == 'd':
            demandnode[row[0]] = int(row[1])
            G.add_node(row[0])
        if row[2] == 's':
            supplynode[row[0]] = int(row[1])        
            G.add_node(row[0])
                
linklist = collections.defaultdict(dict)
capacity = collections.defaultdict(dict)
with open(input('Input the link ')) as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ',') 
    for row in csvreader:
        if (row[0] in removenode) or (row[1] in removenode):
            continue
        linklist[(row[0],row[1])] = int(row[2])
        if float(row[2]) != 0:
            capacity[(row[0],row[1])] = float(row[2])

position = collections.defaultdict(tuple)
demaposi = collections.defaultdict(tuple)
with open(input('Input the location ')) as csvfile2:
    csvreader2 = csv.reader(csvfile2, delimiter = ',')
    for row in csvreader2:
        if row[0] in removenode:
            continue
        position[row[0]] = (float(row[1]),float(row[2]))
        if row[0] in demandnode.keys():
            demaposi[row[0]] = numpy.array([float(row[1]), float(row[2])])
        
colormap = []
for node in G:
    if node in demandnode.keys():
        colormap.append('blue')       
    else:
        colormap.append('green')
        
G.add_edges_from(linklist.keys())
plt.figure(3,figsize=(12,12)) 
networkx.draw_networkx_nodes(G,demaposi,nodelist=demandnode.keys(),node_shape='s')
networkx.draw_networkx(G,position, node_color= colormap, with_labels=True)
plt.show()


from gurobipy import *
dnode, dvalue = multidict(demandnode)
snode, svalue = multidict(supplynode)
link, capa = multidict(capacity)
model = Model ("minimum cost flow problem")

model.setParam('OutputFlag', False)

X = model.addVars(link, vtype = GRB.INTEGER, lb = 0, ub = GRB.INFINITY, name = 'x')
D = model.addVars(dnode, vtype = GRB.CONTINUOUS, lb = 0, ub = GRB.INFINITY, name = 'd')

for i in snode:
    model.addConstr(quicksum(X[i,j] for i, j in link.select(i,'*')) <= supplynode[i])
# Demand constraints
for j in dnode:
    model.addConstr(quicksum(X[i,j] for i, j in link.select('*', j)) == D[j])

# link capacity constraints: maximum capacity
for j in dnode:
    model.addConstr (D[j] <= demandnode[j])  
    
# Define the objective function
Z = quicksum(demandnode[j] - D[j] for j in dnode)/997
model.setObjective(Z, GRB.MINIMIZE)
model.optimize()
if model.status == GRB.OPTIMAL:
    for i, j in link:
        if X[i,j].X != 0:    
            print('From', i, 'to', j, 'is', int(X[i,j].X))

