# Solve the following IP:
#  maximize
#        16 * x1 + 22 * x2 + 12 * x3 + 8 * x4 + 11 * x5 + 19 * x6
#  subject to
#        5 * x1 + 7 * x2 + 4 * x3 + 3 * x4 + 4 * x5 + 6 * x6 <= 14
#        xj binary, j=1,2,...,5,6

import gurobipy as gp
from gurobipy import GRB

# Create a new model
m = gp.Model()

# Create variables
x1 = m.addVar(vtype='B', name="x1")
x2 = m.addVar(vtype='B', name="x2")
x3 = m.addVar(vtype='B', name="x3")
x4 = m.addVar(vtype='B', name="x4")
x5 = m.addVar(vtype='B', name="x5")
x6 = m.addVar(vtype='B', name="x6")

# Set objective function
m.setObjective(50 * x1 + 50 * x2 + 50 * x3 + 8 * x4 + 11 * x5 + 19 * x6, gp.GRB.MAXIMIZE)

# Add constraints
m.addConstr(5 * x1 + 7 * x2 + 4 * x3 + 3 * x4 + 4 * x5 + 6 * x6 <= 14)

# Solve it!
#def subtourelim(model, where):
#    if where == GRB.Callback.MIPSOL:
#        vals = model.cbGetSolution(model._vars)
#        print(vals)

# Add cuts
def myaddcut(model, where):
    if where == GRB.Callback.addCut(x1+x2+x6,GRB.LESS_EQUAL,2):
        vals = model.cbGetSolution(model._vars)
        print(vals)

m.optimize(myaddcut)

print(f"Optimal objective value: {m.objVal}")
print(f"Solution values: x1={x1.X}, x2={x2.X}, x3={x3.X},x4={x4.X}, x5={x5.X}, x6={x6.X},")