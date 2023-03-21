# -*- coding: utf-8 -*-
"""
Assignment3-1

@author: Michael Hu
"""

retailer = ['1','2','3','4','5','6']
warehouse = ['A','B']
demand = [500,800,1800,300,700,900]
supply = [2000,3000]
# combine retailer and demand, combine warehouse and supply
rD = dict(zip(retailer,demand))
wS = dict(zip(warehouse,supply))
#make retailer and warehouse in pair and combine with cost
retailWare = [(x,y) for x in retailer for y in warehouse]
cost = [2,3,4,1,5,3,2,2,1,3,0,0]
rWc = dict(zip(retailWare,cost))

from gurobipy import *

model = Model('Transportation')
model.setParam('OutputFlag', False)
X = model.addVars(retailer, warehouse, vtype = GRB.INTEGER, lb =0, ub =GRB.INFINITY, name ="x")

for i in retailer:
    model.addConstr(quicksum(X[i,j] for j in warehouse) == rD[i])
for j in warehouse:
    model.addConstr(quicksum(X[i,j] for i in retailer) == wS[j])

z = quicksum(X[i,j] * rWc[i,j] for i in retailer for j in warehouse)

model.setObjective(z, GRB.MINIMIZE)


model.optimize()


if model.status == GRB.OPTIMAL:
    print('The mininmum cost is $', int(model.objVal))
    for i in warehouse:
        for j in retailer:
            if j != '6':
                if X[j,i].X != 0:
                    print('Products from W('+ i+')', 'To retailer'+j, 'are', int(X[j,i].X))