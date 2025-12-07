# Vehicle-Management-System-OOP-Project
🚗 Vehicle Management System (OOP Project)

A Python project demonstrating Object-Oriented Programming (OOP) concepts including abstraction, inheritance, polymorphism, encapsulation, and method types.

📌 Project Overview

This project simulates a fleet management system where different types of vehicles (Car, Bike, Truck) are managed by a FleetManager. It showcases:

Abstract classes

Inheritance

Polymorphism

Encapsulation

Instance, class, and static methods

🧩 Features

Vehicle (Abstract Class): Defines common attributes and enforces drive() method.

Car, Bike, Truck (Subclasses): Implement specific driving behavior.

FleetManager: Manages multiple vehicles, adds them to a fleet, and generates reports.

Encapsulation: Protects internal state like fuel level.

Polymorphism: Same method (drive) behaves differently depending on the subclass.

📂 Project Structure

vehicle_system/
│
├── base.py          # Abstract class Vehicle
├── car.py           # Car subclass
├── bike.py          # Bike subclass
├── truck.py         # Truck subclass
├── fleet_manager.py # FleetManager class
├── main.py          # Demo run
└── __init__.py      # Package initializer

🛠️ Example Code

Abstract Class (base.py)

from abc import ABC, abstractmethod

class Vehicle(ABC):
    def __init__(self, brand, year):
        self.brand = brand
        self.year = year
        self._mileage = 0
        self.__fuel_level = 100

    @property
    def mileage(self):
        return self._mileage

    def refuel(self, amount):
        self.__fuel_level += amount

    @abstractmethod
    def drive(self, km):
        pass

    @staticmethod
    def is_motorized():
        return True

    @classmethod
    def from_string(cls, data):
        brand, year = data.split(",")
        return cls(brand, int(year))

Subclass Example (car.py)

from .base import Vehicle

class Car(Vehicle):
    def drive(self, km):
        self._mileage += km
        print(f"Car {self.brand} drove {km} km")

FleetManager (fleet_manager.py)

class FleetManager:
    def __init__(self):
        self.vehicles = []

    def add_vehicle(self, vehicle):
        self.vehicles.append(vehicle)

    def report(self):
        for v in self.vehicles:
            print(f"{v.brand} ({v.year}) - Mileage: {v.mileage}")

Demo Run (main.py)

from car import Car
from bike import Bike
from truck import Truck
from fleet_manager import FleetManager

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

print("\n--- Fleet Report ---")
fleet.report()

🎯 OOP Concepts Demonstrated

Abstraction: Vehicle enforces drive() method.

Inheritance: Car, Bike, Truck inherit from Vehicle.

Polymorphism: drive() behaves differently in each subclass.

Encapsulation: Fuel level hidden with __fuel_level.

Method Types: Instance (drive), Class (from_string), Static (is_motorized).

🚀 How to Run

Clone the repository.

Navigate to the project folder.

Run python main.py.

📖 Interview Notes

Abstraction vs Encapsulation: Abstraction hides implementation, Encapsulation hides data.

Real-life analogy: ATM machine (abstraction), Bank account balance (encapsulation).

This README makes your project professional and interview-ready!:wq
