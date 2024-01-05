# COLLECTION WHICH IS UNORDERED, UNINDEXED AND WITHOUT DUPLICATES

utensils = {"fork", "spoon", "knife", "knife", "knife"}
dishes = {"bowl", "plate", "cup", "knife"}

utensils.add("napkin")

utensils.update(dishes) #! ADDS ALL ELEMENTS
print(utensils)
print(dishes)


dinner_table = dishes.union(utensils)
print(dinner_table)

for i in utensils:
      print(i)

print(utensils.difference(dishes))
print(dishes.difference(utensils))
print(utensils.intersection(dishes))



