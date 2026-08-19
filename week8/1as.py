import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

columns = ['sepal_length', 'sepal_width', 'petal_length', 'petal_width', 'class']
iris = pd.read_csv("IRIS.csv", header=None, names=columns)

x = iris[columns[0]]
xn = np.array(x)
y = iris["class"]
print(x)
