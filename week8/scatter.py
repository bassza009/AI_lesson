import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

columns = ['sepal_length', 'sepal_width', 'petal_length', 'petal_width', 'class']
iris = pd.read_csv("IRIS.csv", header=None, names=columns)

x = iris[columns[0]]
xn = np.array(iris)
y = iris["class"]

plt.figure(figsize=(10, 6))
cls1, cls2, cls3 = iris["class"].unique()

feat1 ,feat2 = 0,3

plt.scatter(xn[y==cls1,feat1], xn[y==cls1,feat2], color='red', label=cls1)
plt.scatter(xn[y==cls2,feat1], xn[y==cls2,feat2], color='green', label=cls2)
plt.scatter(xn[y==cls3,feat1], xn[y==cls3,feat2], color='blue', label=cls3)

plt.xlabel(columns[feat1])
plt.ylabel(columns[feat2])
plt.title("Scatter Plot of Iris Dataset")
plt.legend()
plt.show()