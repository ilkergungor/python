from car import Car

car_1 = Car("Chevy", "Corvette", 2021, "blue")
car_2 = Car("Ford", "Mustang", 2022, "red")

print(car_1.make + " " + car_1.model + " " +str(car_1.year) + " " + car_1.color)
print(car_2.make + " " + car_2.model + " " +str(car_2.year) + " " + car_2.color)

car_1.drive()
car_1.stop()
car_2.drive()
car_2.stop()

car_1.wheels = 2

print(car_1.wheels)
print(car_2.wheels)
print(Car.wheels)
Car.wheels = 2
print(car_1.wheels)
print(car_2.wheels)
print(Car.wheels)

