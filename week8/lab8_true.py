from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.neural_network import MLPClassifier
from sklearn.metrics import accuracy_score
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

train = pd.read_csv("train.csv") #delete data 70-78
test = pd.read_csv("test.csv") #delete data 1-69

x_train,y_train = np.asarray(train.iloc[:,1]).reshape(-1,4),np.array(train.iloc[:,4]).reshape(-1,1)