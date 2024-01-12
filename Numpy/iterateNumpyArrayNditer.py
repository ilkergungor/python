import numpy as np

a = np.arange(12).reshape(3, 4)
print(a)

for row in a:
      print(row)

for row in a:
      for cell in row:
            print(cell)
            
print("--------Flatten--------")

for cell in a.flatten():  #!ABOVE IS SAME AS BELOW
      print(cell)

print("--------NDiter--------")

for i in np.nditer(a, order="C"): #!ABOVE IS SAME AS BELOW 
      print(i)
      
print("--------Fortran--------")
     
for i in np.nditer(a, order="F"): #! F order Fortran style
      print(i)
      
print("--------External Loop--------")

for i in np.nditer(a, order="F", flags=["external_loop"]):
      print(i)
      
print("--------Readwrite--------")

for i in np.nditer(a, order="F", op_flags=["readwrite"]):
      i[...] = i * i
print(a)
      
print("--------Two compatible arrays--------")

b = np.arange(3, 15, 4).reshape(3, 1)
print(b)
      
for x, y in np.nditer(([a, b])):
      print(x, y) #! Until 2nd row of a b has same (3)
 
#!Dimensions of the arrays should be compatible rows and columns
#! a is (3, 4) b is (3, 1) same row numbers
      