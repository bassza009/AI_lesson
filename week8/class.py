import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

columns = ['sepal_length', 'sepal_width', 'petal_length', 'petal_width', 'class']
iris = pd.read_csv("IRIS.csv", header=None, names=columns)

iris_class = iris["class"].unique()
fid = 0
colors = ['red', 'green', 'blue']
makers = ['o', 's', '*']
x = pd.array(x)
y = pd.array(y)
for i,species in enumerate(iris_class):
    spacial_index =  
