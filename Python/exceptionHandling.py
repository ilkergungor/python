try:
      numerator = int (input("Enter a number to divide: "))
      denominator = int (input("Enter a number to divide by: "))
      result = numerator / denominator
except ZeroDivisionError as e:
      print(e)
      print("You can't divide by zero!")
except ValueError as e:
      print(e)
      print("Enter only numbers!") 
except Exception as e:
      print(e)
      print("Something went wrong!")
else:       #!IF THERE IS NO EXCEPTIONS DO THIS
      print(result)
finally:
      print("This will always execute!")
      
      
      