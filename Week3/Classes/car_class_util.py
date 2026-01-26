from car import Car

# Creating three car objects from the Car class which is defined in the car.py file
car1 = Car(2016, "Audi", "Black", True)
car2 = Car(2018, "BMW", "Red", False)
car3 = Car(2019, "Mercedes", "Blue", False)

# To access the attributes of the car objects
print(car1.year)
print(car2.model)   
print(car3.colour)

# To access the methods of the car objects
car1.describe_car()
car2.describe_car()
car3.describe_car()
