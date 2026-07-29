# from sympy import symbols,sympify

# x = symbols("x")
# txt = "(x+2)**2"
# y = sympify(txt)

# print(y.subs(x,1)) #substitube แทนที่ คือเอา 1 แทนด้วย x

# import numpy as np
from sympy import symbols, sympify
formula = []
formula= input("Enter formula : ").split(",")
#formulas.append(formula)


    

for _ in formula :
    x = symbols("x")
    txt = str(_)
    y = symbols(txt)
    print(y.subs(x,1))


