
#! filter() = creates a collection elements from an iterable for
#! which a function returns true
#! filter(function, iterable)

employees = [("Kevin", 35),
                       ("Katy", 39),
                       ("Helena", 40),
                       ("Johnny", 43),
                       ("Victoria", 54),
                       ("Tom", 27)]

age = lambda data: data[1]   >= 40  #!2ND PARAM AGE

party_list = list(filter(age, employees))

for i in party_list:
      print(i)

