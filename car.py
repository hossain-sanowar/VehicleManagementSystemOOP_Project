from __future__ import annotations
import logging
from VehicleManagementSystemOOP_Project.base import Vehicle

logger = logging.getLogger(__name__)


class Car(Vehicle):
    def drive(self, km: int):
        super().drive(km)
        self._mileage += km
        logger.info("Car %s drove %d km", self.brand, km)

    @classmethod
    def from_dict(cls, data: dict) -> "Car":
        car = cls(brand=data["brand"], year=data["year"])
        # restore mileage if provided
        if "mileage" in data:
            m = int(data["mileage"])
            if m < 0:
                raise ValueError("Mileage cannot be negative")
            car._mileage = m
        return car

