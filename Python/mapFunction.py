
#! map() = applies function to list, tuple iterable items
#! map(function, iterable)

store = [("shirt",250.00),    #! ITEMS AND PRICES IN USD
             ("pants", 400.00),
             ("jacket", 750.00),
             ("scarf", 150.00),
             ("belt", 500.00)]

to_euros = lambda data: (data[0], data[1] * 0.95)
to_dollars = lambda data: (data[0], data[1] / 0.95)

store_euros  = list(map(to_euros, store)) #! NORMALLY RETURNS map class

for i in store_euros:
      print(i, end="€\n")
print("\n")

store_dollars =list(map(to_dollars, store_euros))

for i in store_dollars:
      print(i, end="$\n")

      

      
      