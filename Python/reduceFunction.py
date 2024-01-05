
#! reduce() = reducing iterable's single cumulative value
#! performs for first two elements and repeats until 1 value remains

import functools

letters = ["S", "P", "O", "N", "G", "E", " ", "B", "O", "B"]
word = functools.reduce(lambda x, y :x + y, letters)
print(word)

factorial = [8, 7, 6, 5, 4, 3, 2, 1]
result = functools.reduce(lambda a, b :a * b, factorial)
print(result)


