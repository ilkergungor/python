#LOOP CONTROL STATEMENTS

while True:
      type = input("Type anything to end the infinite loop: ")
      if type != "":
            break #! USED TO TERMINATE THE LOOP ENTIRELY
      
print("\n") 

phone_number = "123-456-7890"
for i in phone_number:
      if i == "-":
            continue #! SKIPS TO THE NEXT ITERATION OF THE LOOP
      print(i, end="")  #! IF IT WAS PASS WILL PRINT "-" DASHES AS WELL
      
print("\n")
      
for i in range(1, 21):
      if i == 13:
            pass #! DOES NOTHING, ACTS AS A PLACEHOLDER
      else:
            print(i, end=" ")