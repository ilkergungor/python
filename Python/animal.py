class Animal:
      
      alive = True
      
      def eat(self):
            print("This " + type(self).__name__.lower() + " is eating!")
      
      def sleep(self):
            print("This " + type(self).__name__.lower() + " is sleeping!")
            
            
class Rabbit(Animal):
      def run(self):
            print("This " + type(self).__name__.lower() + " is running!")
            
class Fish(Animal):
      def swim(self):
            print("This " + type(self).__name__.lower() + " is swimming!")
            
class Hawk(Animal):
      def fly(self):
            print("This " + type(self).__name__.lower() + " is flying!")

rabbit = Rabbit()
fish = Fish()
hawk = Hawk()

print(rabbit.alive)
fish.eat()
hawk.sleep()

rabbit.run()
fish.swim()
hawk.fly()



