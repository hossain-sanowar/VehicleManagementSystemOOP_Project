from __future__ import annotations
import logging
from VehicleManagementSystemOOP_Project.base import Vehicle

logger = logging.getLogger(__name__)


class Bike(Vehicle):
    def drive(self, km: int):
        super().drive(km)
        self._mileage += km
        logger.info("Bike %s drove %d km", self.brand, km)

    @classmethod
    def from_dict(cls, data: dict) -> "Bike":
        bike = cls(brand=data["brand"], year=data["year"])
        if "mileage" in data:
            m = int(data["mileage"])
            if m < 0:
                raise ValueError("Mileage cannot be negative")
            bike._mileage = m
        return bike

