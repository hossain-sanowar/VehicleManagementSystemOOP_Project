from abc import ABC, abstractmethod

class Vehivle(ABC):
    def __init__(self, brand, year):
        self.brand=brand
        self.year=year
        self._mileage=0
        self.__fuel_level=100


    @property
    def mileage(self):
        return self._mileage

    def refuel(self, amount):
        self.__fuel_level +=amount


    @abstractmethod
    def drive(self, km):
        pass

    @staticmethod
    def is_motorized():
        return True

    @classmethod
    def from_string(cls,data):
        brand, year = data.split(",")
        return cls(brand, int(year))

