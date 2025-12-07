from __future__ import annotations
import json
import logging
from typing import List, Type

from VehicleManagementSystemOOP_Project.base import Vehicle
from VehicleManagementSystemOOP_Project.car import Car
from VehicleManagementSystemOOP_Project.bike import Bike
from VehicleManagementSystemOOP_Project.truck import Truck

logger = logging.getLogger(__name__)


TYPE_REGISTRY: dict[str, Type[Vehicle]] = {
    "Car": Car,
    "Bike": Bike,
    "Truck": Truck,
}


class FleetManager:
    def __init__(self):
        self.vehicles: List[Vehicle] = []

    def add_vehicle(self, vehicle: Vehicle):
        if not isinstance(vehicle, Vehicle):
            raise TypeError("Only Vehicle instances can be added to the fleet")
        self.vehicles.append(vehicle)
        logger.info("Added %s (%s) to fleet", vehicle.brand, vehicle.__class__.__name__)

    def report(self):
        for v in self.vehicles:
            print(f"{v.brand} ({v.year}) - Mileage: {v.mileage}")

    def to_dict(self) -> list[dict]:
        return [v.to_dict() for v in self.vehicles]

    def save_fleet(self, filename: str = "fleet.json"):
        data = self.to_dict()
        with open(filename, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=2)
        logger.info("Fleet saved to %s", filename)

    def load_fleet(self, filename: str = "fleet.json"):
        try:
            with open(filename, "r", encoding="utf-8") as f:
                data = json.load(f)
        except FileNotFoundError:
            logger.warning("No fleet file found at %s; starting from empty fleet", filename)
            return

        self.vehicles.clear()
        for item in data:
            t = item.get("type")
            cls = TYPE_REGISTRY.get(t)
            if not cls:
                logger.warning("Skipping unknown vehicle type: %s", t)
                continue
            vehicle = cls.from_dict(item)
            self.vehicles.append(vehicle)
        logger.info("Fleet loaded from %s (%d vehicles)", filename, len(self.vehicles))

