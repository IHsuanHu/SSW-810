# -*- coding: utf-8 -*-
"""
Assignment3-2

@author: Michael Hu
"""

warehouse = ['Tampa', 'Miami', 'Fresno']
market = ['New York', 'Philadelphia', 'Chicago', 'Boston']
#warehouse supply
wS = {i:200 for i in warehouse}
demand = [130,170,100,150]
#market demand
mD = dict(zip(market,demand))
cost = [9,11,12,14,10,8,12,6,15,17,10,7]
#make market and warehouse in pair and combine with cost
wM = [(x,y) for y in market for x in warehouse]
wMc = dict(zip(wM,cost))


from gurobipy import *

model = Model('Transportation Cost')
model.setParam('OutputFlag', False)

X = model.addVars(warehouse, market, vtype = GRB.INTEGER, lb = 0, ub = GRB.INFINITY, name = 'x')
#supply and demand are unequal
for i in warehouse:
    model.addConstr(quicksum(X[i,j] for j in market) <= wS[i])
for j in market:
    model.addConstr(quicksum(X[i,j] for i in warehouse) == mD[j])

#if i != 'Miami' and j != 'Chicago' continue
z = quicksum(X[i,j] * wMc[i,j] for i in warehouse for j in market if i != 'Miami' and j != 'Chicago')

model.setObjective(z, GRB.MINIMIZE)

model.optimize()


if model.status == GRB.OPTIMAL:
    print('The minimmum cost of the transportation is $'+str(int(model.objVal)) + '00')
    for i in warehouse:
        for j in market:
            if X[i,j].X != 0:
                print('Oranges from', i, 'to', j, 'are', int(X[i,j].X))