# lambda parameters: expression

def double(x):
      return x * 2

print(double(4))

triple = lambda x: x * 3
print(triple(6))

multiple = lambda x, y: x * y
print(multiple(7, 8))

add = lambda a, b, c: a + b + c
print(add(16, 32, 64))

full_name = lambda first_name, last_name: first_name + " " + last_name
print(full_name("Sponge", "Bob"))

age_check = lambda age:True if age >= 18 else False
print(age_check(18))


