import numpy as np

n = [4, 5, 6]
print(n[0:2])
print(n[-1])

print("-----------------")

array = np.array([4, 5, 6])
print(array[0:2])
print(array[-1])

print("/////////////////////")

a= np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

print(a[2,2]) #! Matrix Index

print(a[0: 3, 2]) #! 0 to 2 last elements

print("++++++++++")

print(a[-1])#! Last element

print(a[-1, 0:2]) #! row is -1 (means last), 0:2 column is 0 to 2

print("-------------------")
print(a[:, 1:3]) #! all row and 1:3 columns

