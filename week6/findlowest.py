# import numpy as np
from sympy import symbols, sympify
formula = []
formula= input("Enter formula : ").split(",")
#formulas.append(formula)


    
x = symbols("x")
y = symbols("y")
low = 1
for _ in formula :
    txt = _
    ei = sympify(txt)    
    print(ei.subs({x:low,y:low}))



# (x-2)*(x-2)+(y+1)*(y+1),2*(x-2),2*(y+1)