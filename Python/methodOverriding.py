class Animal:

      def eat(self):
            print("This " + type(self).__name__.lower() + " is eating!")
      
      def sleep(self):
            print("This " + type(self).__name__.lower() + " is sleeping!")
            
class Rabbit(Animal):
      def eat(self):
            print("This " + type(self).__name__.lower() + " is eating too much carrot!")
            
      def sleep(self):
            print("This " + type(self).__name__.lower() + " is sleeping too much!")
                    
rabbit = Rabbit()
rabbit.eat()
rabbit.sleep()



