import numpy as np

a= np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(a)

for row in a:
      print(row)
      
print("--------Cell--------")

for cell in a.flat:
      print(cell)
      
print("--------Reshape--------") 
      
a = np.arange(6).reshape(3, 2)
print(a)

b = np.arange(6, 12).reshape(3, 2)
print(b)

print("--------Vstack--------") #! Vertical

c = np.vstack((a, b))
print(c)

print("--------Hstack--------") #! Horizontal

c = np.hstack((a, b))
print(c)

print("- - - - - - - - - - - - - - - -") 

a = np.arange(30).reshape(2, 15)
print(a)

print("--------Hsplit--------") 

h = np.hsplit(a, 3) #! 3 new horizontal same size arrays
print(h)
print(h[0])
print(h[1])
print(h[2])

print("--------Vsplit--------") 

v = np.vsplit(a, 2) #! 2 new vertical same size arrays
print(v)
print(v[0])
print(v[1])






