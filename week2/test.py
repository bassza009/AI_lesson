import numpy as np

# create two matrics
#metrix_a = np.array([[1,2,3],
#                     [4,5,6],
#                     [7,8,9]])

#metrix_b = np.array([[9,8,7],
#                     [6,5,4],
#                     [3,2,1]])

#Metrix multiplication
#result_multiplication = np.matmul(metrix_a, metrix_b)

#Metrix dot product
#result_dot_product = np.dot(metrix_a,metrix_b)

#Display

#print(f"Metrix a : {metrix_a}")
#print(f"Metrix b : {metrix_b}")

#print(f"Metrix multiplication : {result_multiplication}")
#print(f"Metrix dot product : {result_dot_product}")


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