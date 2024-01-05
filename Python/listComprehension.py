
#!list comprehension create new list with less code
#! certain lambda functions [iterable items if conditional]

squares = []
for i in range(1, 11):
      squares.append(i* 1)
print(squares)

#!ABOVE IS SAME AS BELOW

squares = [i * 1 for i in range(1, 11)]
print(squares)

#!\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\

scores = [20, 80, 50, 100, 10, 40, 70, 30, 90, 0, 60]

passed = list(filter(lambda x: x>= 60, scores))
passed.sort(reverse=True)
print(passed)

#!ABOVE IS SAME AS BELOW

passed2 = [i for i in scores if i >= 60]
passed2.sort(reverse=True)
print(passed2)

#!ABOVE IS SAME AS BELOW

passed3 = [i if i >= 60 else  "FF" for i in scores]
print(passed3)





