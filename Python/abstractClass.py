from abc import ABC,  abstractmethod

class Vehicle(ABC):     #! (ABC) ABSTRACT METHOD DECLARATION WITHOUT IMPLEMENTATION

      @abstractmethod
      def go(self):     
            pass

      @abstractmethod
      def stop(self):
            pass

class Car(Vehicle):

      def go(self):
            print("You drive the " + type(self).__name__.lower() +  "!")

      def stop(self):    
            print("The " + type(self).__name__.lower() + " is stopped!") 

class Motorcycle(Vehicle):

      def go(self):
            print("You ride the " + type(self).__name__.lower() +  "!")

      def stop(self):    
            print("The " + type(self).__name__.lower() + " is stopped!") 

car = Car()
motorcycle = Motorcycle()

car.go()
car.stop()

motorcycle.go()
motorcycle.stop()




