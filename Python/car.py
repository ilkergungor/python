class Car:
      
      wheels = 4 #! CLASS VARIABLE
      
      def __init__(self, make, model, year, color):
            self.make = make  #! INSTANCE VARIABLE
            self.model = model #! INSTANCE VARIABLE
            self.year = year #! INSTANCE VARIABLE
            self.color = color #! INSTANCE VARIABLE
      
      def drive(self):
            print("This " + self.color + " " + self.model + " is driving!")
            
      def stop(self):
            print("This " + self.color + " " + self.model + " stopped!")

