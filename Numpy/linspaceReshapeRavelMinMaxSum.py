import  numpy as np

a = [np.linspace(22, 60, 9)] #linearly 
print(a)

a = [np.linspace(0, 1, 4)] #linearly 
print(a)


array = np.array([[12, 34, 56], [78, 96, 107], [118, 129, 140]])
print(array.shape)

array = array.reshape(1,9) #! Now it's a one dimensional array
print(array)

array = array.reshape(9, 1) #! Now it's a one dimensional array
print(array)

array = array.ravel() #! Again it's a one dimensional array by ravel flatten function
print(array)

print(array.min())
print(array.max())
print(array.sum())

array = np.array([[12, 34, 56], [78, 96, 107], [118, 129, 140]])
print(array.sum(axis=0))
print(array.sum(axis=1))
print(np.sqrt(array)) #! SQRT for each number
print(np.std(array)) #! Standard Deviation of an array

