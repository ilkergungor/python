class Duck:
      def walk(self):
            print("The duck walks!")
      
      def talk(self):
            print("The duck is qwuacking!")
            
class Chicken:
      def walk(self):
            print("The chicken walks!")
      
      def talk(self):
            print("The chicken is clucking!")
            
class Person():
      def catch(self, duck):
            duck.walk()
            duck.talk()
            print("You caught the " + type(duck).__name__.lower() + "!")
            
duck = Duck()
chicken = Chicken()
person = Person()

person.catch(duck)   
person.catch(chicken)   
#! METHODS ARE MORE IMPORTANT THAN AN OBJECT


