# MULTIPLE ITEMS IN A SINGLE VARIABLE

food = ["pizza", "hamburger", "hotdog", "pasta"]
print(food)

food[2]  = "sushi"
print(food[2])

for i in food:
      print (i)
      
food.append("ice cream")
print(food)
food.pop()
print(food)

food.insert(0, "cake")
print(food)

food.sort()
print(food)

food.clear()
print(food)


