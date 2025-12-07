from car import Car
from bike import Bike
from truck import Truck
from fleet_manager import FleetManager

car=Car("BMW", 2020)
bike = Bike("Yamaha", 2019)
truck = Truck("Volvo", 2021)


car.drive(50)
bike.drive(20)
truck.drive(100)


fleet=FleetManager()
fleet.add_vehicle(car)
fleet.add_vehicle(bike)
fleet:add_vehicle(truck)


print("\n--- Fleet Report ----")
fleet.report()
