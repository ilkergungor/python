class Car:
      color = None
      
class Motorcycle :
      color= None
      
def change_Color(car, color):
      car.color = color
      
car_1 = Car()
car_2 = Car()
car_3 = Car()

bike_1 = Motorcycle()

change_Color(car_1, "red")
change_Color(car_2, "green")
change_Color(car_3, "blue")
change_Color(bike_1, "black")

print(car_1.color)
print(car_2.color)
print(car_3.color)
print(bike_1.color)

