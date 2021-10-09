from project.car import Car


class SportCar(Car):
    DEFAULT_FUEL_CONSUMPTION = 10


sport = SportCar(50, 150)
print(sport.DEFAULT_FUEL_CONSUMPTION)
print(sport.fuel)
print(sport.horse_power)
print(sport.fuel_consumption)
sport.drive(1)
print(sport.fuel)
