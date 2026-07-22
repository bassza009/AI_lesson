import numpy as np
from matplotlib import pyplot as plt

def steepest(initial_guess, learning_rate , iterations):
    x ,y = initial_guess
    fx = []
    for i in range(iterations):
        gradient = np.array([2 * (x-2),2 * (y+1)])
        update = -learning_rate* gradient
        x, y = x + update[0],y + update[1]

        _fx = (x-2)**2+(y+1)**2
        print(f"Iteration {i+1} : x = {x:.4f}, f(x,y) = {_fx:.4f}")
        fx.append(_fx)
    return x,y,fx

initial_guess = [0,0]
learning_rate = 0.001
iteration = 1000

lx,ly ,fx = steepest(initial_guess,learning_rate,iteration)
x = range(len(fx))
plt.plot(x,fx)
plt.show()