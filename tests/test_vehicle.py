import pytest
from VehicleManagementSystemOOP_Project.car import Car
from VehicleManagementSystemOOP_Project.bike import Bike
from VehicleManagementSystemOOP_Project.truck import Truck


def test_vehicle_drive_positive():
    car = Car("TestBrand", 2020)
    car.drive(10)
    assert car.mileage == 10


def test_vehicle_drive_invalid():
    bike = Bike("Brand", 2020)
    with pytest.raises(ValueError):
        bike.drive(0)
    with pytest.raises(ValueError):
        bike.drive(-5)


def test_vehicle_refuel():
    truck = Truck("Brand", 2020)
    truck.refuel(10)
    assert truck.fuel_level == 100  # starts at 100, capped


def test_vehicle_invalid_brand_year():
    with pytest.raises(ValueError):
        Car("", 2020)
    with pytest.raises(ValueError):
        Car("Brand", 1500)

