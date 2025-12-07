from __future__ import annotations
import logging
from VehicleManagementSystemOOP_Project.base import Vehicle

logger = logging.getLogger(__name__)


class Truck(Vehicle):
    def drive(self, km: int):
        super().drive(km)
        # example: trucks consume more fuel; just mileage update here
        self._mileage += km
        logger.info("Truck %s drove %d km", self.brand, km)

    @classmethod
    def from_dict(cls, data: dict) -> "Truck":
        truck = cls(brand=data["brand"], year=data["year"])
        if "mileage" in data:
            m = int(data["mileage"])
            if m < 0:
                raise ValueError("Mileage cannot be negative")
            truck._mileage = m
        return truck

