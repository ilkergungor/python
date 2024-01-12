import numpy as np

a = np.array([12, 54, 76])
print(a)

a = np.array([[12, 34, 56], [78, 96, 107], [118, 129, 140]]) #!Multi dimensional with two braces

print(a)

print(a.ndim) #! Number of dimensions
print(a.dtype)
print("Itemsize = ",a.itemsize)

a = np.array([[12, 34, 56], [78, 96, 107], [118, 129, 140]], dtype=np.float64)

print(a.dtype)
print("Itemsize = ",a.itemsize)
print(a) #! Float numbers with  end  by a dot
print(a.size) #! Size is 9
print(a.shape) #! Shape 3 x 3 matrix

a = np.array([[12, 34, 56], [78, 96, 107], [118, 129, 140]], dtype=complex)
print(a) 

