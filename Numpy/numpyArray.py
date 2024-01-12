import numpy as numpy
import time as time
import sys

a = numpy.array([1,2,3])    #! Less memory usage, fast working, convenient
# print(a[0] + a[1] + a[2])

list = range(1000)
print(sys.getsizeof(5) * len(list))

array = numpy.arange(1000)             #! similar to range
print(array.size * array.itemsize) #! size is less than python, that's why python is slow

SIZE = 100000

list1 = range(SIZE)
list2 = range(SIZE)

array1 = numpy.arange(SIZE)
array2 = numpy.arange(SIZE)

#!PYTHON LISTS TIME CALCULATING

start = time.time()
result = [(x+y) for x,y in zip(list1, list2)]
print("Python list took about: " , (time.time() - start) * 1000)

#!NUMPY ARRAYS TIME CALCULATING

start = time.time()
result = array1 + array2
print("Numpy array took about: " , (time.time() - start) * 1000)

a1 = numpy.array([1,2,3])
a2 = numpy.array([4,5,6])
print(a1*a2)
print(a1+a2)
print(a1/ a2)


