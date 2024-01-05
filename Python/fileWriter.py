text = "Lorem Ipsum\n"
try:
      with open('writtenFile.txt', 'w') as file:  #! w = OVERWRITE
            file.write(text)
            
      with open('writtenFile.txt', 'a') as file:  #! a = APPEND
            file.write(text)
            
      with open('writtenFile.txt', 'r') as file:  #! r =READ
            print(file.read())
except FileNotFoundError as e:
     print(e)
