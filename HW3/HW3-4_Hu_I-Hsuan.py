# -*- coding: utf-8 -*-
"""
Assignment3-4

@author: Michael Hu
"""

event = ['Alumni Brunch', 'Parents\' Brunch','Booster Club Lunch', 'Postgame Party', 'Lettermen\'s Dinner', 'Countributors\' Dinner']
caterer = ['AI\'s', 'Bon Apetit', 'Custom', 'Divine', 'Epicurean', 'Fouchess', 'University']
#constraint of event
eventsessions = {i:1 for i in event}
#caterers' capacity
capacity = [1,2,2,1,1,1,2]
catCap = dict(zip(caterer,capacity))
#the cost of the event and caterer
eventcater = [(i,j) for i in event for j in caterer]
cost = [12.6,14.5,13.0,11.5,10.8,13.5,12.5,10.3,13.0,14.0,12.6,11.9,13.5,14.3,
        14.0,16.5,17.6,13.0,12.9,15.5,16.0,19.5,17.0,21.5,18.7,17.5,22.3,22.0,
        25.0,22.5,23.0,26.2,21.9,24.5,26.7,30.0,32.0,35.0,33.5,28.5,36.0,34.0]

eCcost = dict(zip(eventcater,cost))


from gurobipy import *
model = Model('Cater cost')
model.setParam('OutputFlag', False)

X = model.addVars(event, caterer, vtype = GRB.INTEGER, lb = 0, ub = GRB.INFINITY, name = 'x')

for i in event:
    model.addConstr(quicksum(X[i,j] for j in caterer) == eventsessions[i])
for j in caterer:
    model.addConstr(quicksum(X[i,j] for i in event) <= catCap[j])
    
z = quicksum(X[i,j] * eCcost[i,j] for i in event for j in caterer)

model.setObjective(z, GRB.MINIMIZE)
model.optimize()


if model.status == GRB.OPTIMAL:
    print('The lowest total cost is $', model.objVal)
    for i in event:
        for j in caterer:
            if X[i,j].X != 0:
                print(i,'will be held in',j)

