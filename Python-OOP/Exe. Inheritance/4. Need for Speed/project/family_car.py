from project.car import Car


class FamilyCar(Car):
    pass


# family_car = FamilyCar(150, 150)
# print(family_car.fuel)
# print(family_car.fuel_consumption)
# family_car.drive(50)
# print(family_car.fuel)

family_car = FamilyCar(150, 150)
family_car.drive(50)
print(family_car.fuel)
family_car.drive(50)
print(family_car.fuel)
print(family_car.__class__.__bases__[0].__name__)
