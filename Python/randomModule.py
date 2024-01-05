import random

x = random.randint(1, 6) #! DICE
print(x)

y = random.random() #! INTERVAL [0, 1)
print(y)

my_list = ['rock', 'paper', 'scissors']
z = random.choice(my_list)

cards = [1, 2, 3, 4, 5, 6, 7, 8, 9, 'J', 'Q', 'K', 'A']
random.shuffle(cards)
print(cards)



