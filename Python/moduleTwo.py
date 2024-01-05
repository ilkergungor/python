import moduleOne

print(__name__)
print(moduleOne.__name__)

if __name__ == "__main__":
      print("Module running directly!")
else:
      print("Running another directly!")
      
      #! __name__ is special variable, is "__main__" 
      
      