import os

location = "C:\\Users\\lkrgn\\OneDrive\\Documents\\questions.txt"

if os.path.exists(location):
      print("That location exists!")
      if os.path.isfile(location):
            print("That is a file!")
      elif os.path.isdir(location):
            print("That is a directory!")
else: 
      print("That location doesn't exists!")
      
      
      
      
      