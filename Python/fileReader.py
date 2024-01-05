try:
      with open('questions.txt') as file:
            print(file.read())
            print(file.closed)
except FileNotFoundError as e:
     print(e)
     
      
