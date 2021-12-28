#!/usr/bin/env python3.8

# Copyright 2021, Haoyu Miao

import gurobipy as gp
from gurobipy import GRB


try:
    MP = gp.Model() # Benders Master Problem
    y = MP.addVars(3,vtype=GRB.BINARY,name="y")
    x = MP.addVars(2,vtype=GRB.CONTINUOUS,name="x",lb=0)
    MP.update()
    x[0].obj = 2
    MP.setObjective(x[0] + x[1],sense=GRB.MAXIMIZE)
    # MP.addConstr(x[0] + 2 * x[1] >= 1)
    # MP.addConstr(2 * x[0] + x[1] >= 1)
    MP.addConstr(x[0] >= 1)
    MP.addConstr(x[1] >= 1)
    MP.Params.InfUnbdInfo = 1

    MP.optimize()
    if MP.status == GRB.Status.UNBOUNDED:
        ray = MP.UnbdRay
        print(ray)
        print("Wow, Unbounded!")



except gp.GurobiError as e:
    print('Error code ' + str(e.errno) + ": " + str(e))

except AttributeError:
    print('Encountered an attribute error')



