# import numpy as np
from sympy import symbols, sympify,solve
formula = []
formula= input("Enter formula : ").split(",")
#formulas.append(formula)


    
x = symbols("x")
y = symbols("y")
objective_function = sympify(formula[0])
df_x = sympify(formula[1])
df_y = sympify(formula[2])

critical = solve((df_x,df_y),(x,y))
min_value = objective_function.subs(critical)

print(min_value)
# for _ in formula :
#     txt = _
#     ei = sympify(txt)    
#     print(ei.subs({x:low,y:low}))



# (x-2)*(x-2)+(y+1)*(y+1),2*(x-2),2*(y+1)
# x*x+2*x*y+3*y*y-4*x-5*y+6,2*x+2*y-4,6*y+2*x-5 