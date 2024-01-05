
#! sort method is for lists
#! sort function is for iterables

characters = ["C", "K", "P", "A", "S", "D", "E", "G", "X"]

characters.sort(reverse=True)

for i in characters:
      print(i, end=" ")

print("\n-----------------------------------------------\n")      

numbers = [8765743, 3432, 45, 98736453, 495956, 12534, 5, 765, 9874731]

sorted_numbers = sorted(numbers)

for i in sorted_numbers:
      print(i, end=" ")

print("\n-----------------------------------------------\n")     

answers = [("SECOND", "B", 5),      #! "SORTING STRING", "LETTER", INTEGER
                  ("FOURTH", "D", 2),
                  ("FIFTH", "E", 3),
                  ("FIRST", "A", 4),
                  ("THIRD", "C", 1)]

answers.sort()    #!SORTS BY FIRST PARAM OF TUPLES
for i in answers:
      print(i)

print("\n-----------------------------------------------\n")    

integer = lambda integers: integers[2]  #!SORTS BY THIRD PARAM OF TUPLES
answers.sort(key= integer)

for i in answers:
      print(i)

print("\n-----------------------------------------------\n")    

letter = lambda letters: letters[1]  #!SORTS REVERSE BY SECOND PARAM OF TUPLES
answers.sort(key= letter, reverse=True)

for i in answers:
      print(i)

print("\n-----------------------------------------------\n")    

questions = (("SECOND", "B", 5),      #! TUPLE
                  ("FOURTH", "D", 2),
                  ("FIFTH", "E", 3),
                  ("FIRST", "A", 4),
                  ("THIRD", "C", 1))

int = lambda ints: ints[2] 
sorted_answers = sorted(answers, key=int)

for i in sorted_answers:
      print(i)


