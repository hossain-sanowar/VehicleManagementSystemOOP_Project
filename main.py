from VehicleManagementSystemOOP_Project.car import Car
from VehicleManagementSystemOOP_Project.bike import Bike
from VehicleManagementSystemOOP_Project.truck import Truck
from VehicleManagementSystemOOP_Project.fleet_manager import FleetManager


def main():
    car = Car("BMW", 2020)
    bike = Bike("Yamaha", 2019)
    truck = Truck("Volvo", 2021)

    car.drive(50)
    bike.drive(20)
    truck.drive(100)

    fleet = FleetManager()
    fleet.add_vehicle(car)
    fleet.add_vehicle(bike)
    fleet.add_vehicle(truck)

    print("\n--- Fleet Report ----")
    fleet.report()


if __name__ == "__main__":
    main()

