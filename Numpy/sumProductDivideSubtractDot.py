import numpy as np

array1 = np.array([[1, 2], [3, 4]])
array2 = np.array([[5, 6], [7, 8]])
print(array1, array2)

print("Add ")

array3 = array1 + array2
print(array3)
print("Product")

print(array1 * array2)
print("Divide")
print(array1 / array2)
print("Subtract")
print(array1 - array2)

print("Matrix Product") #! 1*5 + 2* 7 = 19...
print(array1.dot((array2)))

