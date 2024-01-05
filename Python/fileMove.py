import os

source = 'test.txt'
destination = 'C:\\PY\\test.txt'

try:
      if os.path.exists(destination):
            print("There is already a file in this location.")
      else:
            os.replace(src=source, dst=destination)
            print(source + " was moved to " + destination +" destination!")
            
except FileNotFoundError as e:
      print(e)
      