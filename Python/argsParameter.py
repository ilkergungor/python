
#! *args = parameter that will pack all arguments into a tuple

def add(*args):
      sum = 0
      
      for i in args:
            sum += i
      return sum
      
print(add(1, 2, 3, 4, 5, 6, 7, 8, 9, 10))

def addStuff(*stuff):
      stuff = list(stuff)      #! stuff = list(stuff)
      sum = 1           #! MUST BE CAST TO A CHANGEABLE COLLECTION, TUPLES NOT CHANGEABLE
      stuff[0] = 1      
                             
      for i in stuff:
            sum *= i
      return sum
      
print(addStuff(1, 2, 3, 4, 5, 6, 7, 8))



