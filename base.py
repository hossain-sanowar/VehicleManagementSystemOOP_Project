from __future__ import annotations
from abc import ABC, abstractmethod
import logging

logger = logging.getLogger(__name__)


class Vehicle(ABC):
    def __init__(self, brand: str, year: int):
        if not brand or not isinstance(brand, str):
            raise ValueError("brand must be a non-empty string")
        if not isinstance(year, int) or year < 1886:  # first car ~1886
            raise ValueError("year must be an integer >= 1886")
        self.brand = brand
        self.year = year
        self._mileage = 0
        self.__fuel_level = 100  # encapsulated example

    @property
    def mileage(self) -> int:
        return self._mileage

    @property
    def fuel_level(self) -> int:
        # read-only public view (encapsulation)
        return self.__fuel_level

    def refuel(self, amount: int):
        if not isinstance(amount, int) or amount <= 0:
            raise ValueError("Refuel amount must be a positive integer")
        self.__fuel_level = min(100, self.__fuel_level + amount)
        logger.debug("Refueled %s: +%d -> %d", self.brand, amount, self.__fuel_level)

    @abstractmethod
    def drive(self, km: int):
        if not isinstance(km, int) or km <= 0:
            raise ValueError("Drive distance must be a positive integer")

    @staticmethod
    def is_motorized() -> bool:
        return True

    @classmethod
    def from_dict(cls, data: dict) -> Vehicle:
        # Used by FleetManager.load_fleet for polymorphic construction in subclasses
        return cls(brand=data["brand"], year=data["year"])

    def to_dict(self) -> dict:
        return {
            "type": self.__class__.__name__,
            "brand": self.brand,
            "year": self.year,
            "mileage": self._mileage,
            "fuel_level": self.fuel_level,
        }

