class Organism:

      alive = True

class Animal(Organism):
      def eat(self):
            print("This " + type(self).__name__.lower() + " is eating!")

class Dog(Animal):
      def bark(self):
            print("This " + type(self).__name__.lower() + " is barking!")

dog = Dog()
print(dog.alive)
dog.eat()
dog.bark()



