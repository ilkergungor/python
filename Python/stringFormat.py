animal = "cow"
item="moon"

print("The "+ animal + " jumped over the " + item)
print("The {} jumped over the {}".format("horse", "car")) 
print("\nThe {1} jumped over the {0}".format(item, animal))  #! POSITIONAL ARGUMENT
print("The {animal} jumped over the {item}".format(animal= "elephant", item="mars"))  #! KEYWORD ARGUMENT


text = "\nThe {} jumped over the {}"

print(text.format(animal, item))

name = "Sponge"
print("\nHello, my name is {}!".format(name))

print("Hello, my name is {:10}!".format(name))     #! {:10} 10 PADDING
print("Hello, my name is {:<10}!".format(name))   #!AFTER
print("Hello, my name is {:>10}!".format(name))   #!BEFORE
print("Hello, my name is {:^10}!".format(name))   #!CENTER

pi = 3.14159
print("\nThe number pi is {:.2f} ".format(pi)) #! FIRST 2 DIGITS

number = 123456789
print("\nThe number is {:.3f} ".format(number)) #! 3 MORE DIGITS AFTER DOT
print("The number is {:,} ".format(number)) #! SHOWS COMMAS EVERY 3 DIGITS

print("\nThe number is {:b} ".format(number)) #! BINARY
print("The number is {:o} ".format(number)) #! OCTAL

print("\nThe number is {:X} ".format(number)) #! UPPER CASE HEXADECIMAL
print("The number is {:x} ".format(number)) #! LOWER CASE HEXADECIMAL

print("\nThe number is {:e} ".format(number)) #! SCIENTIFIC NOTATION
print("The number is {:E} ".format(number)) #! SCIENTIFIC NOTATION






