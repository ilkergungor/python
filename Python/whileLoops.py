
#? while 1==1: print("Hello! I'm stuck in a loop!")

name = ""

while len(name) == 0:
      name = input("Enter a name: ")
      
print("Hello " + name)

#!ABOVE IS SAME AS BELOW

name = None

while not name:
      name = input("Enter a name: ")
      
print("Hello " + name)


