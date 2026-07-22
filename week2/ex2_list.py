import numpy as np

a = [3,5,85,41,23,6,1]
print(f"a : {a}")
a.sort(reverse=False)
# return a as sort list ascending
print(f"a after sort {a}")

a = [6,1,5,7,9,10]
print(f"new a : {a}")
indx = np.argsort(a)
#Return index of sorting array
print(f"index : {indx}")

#convert list a to np array
print(np.array(a)[indx])
