#! **kwargs = parameter that will pack all arguments into a dictionary

def hello(**kwargs):        #! WITH KWARGS   FUNCTION CAN ACCEPT VARYING AMOUNT OF ARGUMENTS
      #print("Hello " + kwargs["first"] + " " + kwargs["last"])
      
      print("Hello", end=" ")
      for key, value in kwargs.items():
            print(value, end=" ")         #! end=" " PREVENTS NEXT LINES FOR EACH PARAMS
      
hello(title="Mr.", first="Sponge", middle="Middlename", last="Bob")




