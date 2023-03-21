# -*- coding: utf-8 -*-
"""
Assignment3-3

@author: Michael Hu
"""

farm = ['Ohio', 'Pennsylvania', 'New York']
plant = ['Indiana', 'Georgia']
distribution = ['Virginia', 'Kentucky', 'Louisiana']
supply = [72, 105, 83]
demand = [90, 80, 120]
pC = {i:140 for i in plant}
fS = dict(zip(farm,supply))
dD = dict(zip(distribution,demand))
fP = [(i,j) for i in farm for j in plant]
cost1 = [16,21,18,16,22,25]
pD = [(i,j) for i in plant for j in distribution]
cost2 = [23,15,29,20,17,24]
fPdC = dict(zip(fP+pD,cost1+cost2))

from gurobipy import *

model = Model('Transportation cost')
model.setParam('OutputFlag', False)

X = model.addVars(farm, plant, vtype = GRB.INTEGER, lb = 0, ub = GRB.INFINITY, name = 'x')
Y = model.addVars(plant, distribution, vtype = GRB.INTEGER, lb = 0, ub = GRB.INFINITY, name = 'y')

for i in farm:
    model.addConstr(quicksum(X[i,j] for j in plant) == fS[i])
for j in distribution:
    model.addConstr(quicksum(Y[i,j] for i in plant) <= dD[j])
for i in plant:
    model.addConstr(quicksum(X[j,i] for j in farm) == quicksum(Y[i,j] for j in distribution))
for i in plant:
    model.addConstr(quicksum(X[j,i] for j in farm) <= pC[i])

    
z = quicksum(X[i,j] * fPdC[i,j] for i in farm for j in plant) + quicksum(Y[i,j] * fPdC[i,j] for i in plant for j in distribution)
model.setObjective(z, GRB.MINIMIZE)

model.optimize()


if model.status == GRB.OPTIMAL:
    print('The minimum cost of transportation is $'+str(int(model.objVal)))
    for i in farm:
        for j in plant:
            if X[i,j].X != 0:    
                print('Grapes from', i, 'to', j, 'are', str(int(X[i,j].X))+',000 tons')
    for i in plant:
        for j in distribution:
            if Y[i,j].X != 0:
                print('Juice from', i, 'to', j, 'is', str(int(Y[i,j].X))+',000 tons')


    
    
    
    
