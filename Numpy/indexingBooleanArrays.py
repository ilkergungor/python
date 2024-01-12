import numpy as np
      
a = np.arange(12).reshape(3, 4)
print(a)

b = a > 4
print(b)

print(a[b])

a[b] = -1 #! All true booleans assigned to -1
print(a)


