from __future__ import annotations
import argparse
import logging
import sys

from VehicleManagementSystemOOP_Project.car import Car
from VehicleManagementSystemOOP_Project.bike import Bike
from VehicleManagementSystemOOP_Project.truck import Truck
from VehicleManagementSystemOOP_Project.fleet_manager import FleetManager


def setup_logging(verbosity: int):
    # Map verbosity to logging levels
    level = logging.WARNING
    if verbosity == 1:
        level = logging.INFO
    elif verbosity >= 2:
        level = logging.DEBUG

    logging.basicConfig(
        level=level,
        format="%(asctime)s | %(levelname)s | %(name)s | %(message)s",
        stream=sys.stdout,
    )
    logging.getLogger("VehicleManagementSystemOOP_Project").setLevel(level)


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        prog="VehicleManagementSystemOOP_Project",
        description="Vehicle Management System with OOP, logging, persistence, and CLI",
    )
    parser.add_argument(
        "-v", "--verbose", action="count", default=0,
        help="Increase verbosity (-v for INFO, -vv for DEBUG)"
    )

    subparsers = parser.add_subparsers(dest="command", required=False)

    # add vehicle
    add_parser = subparsers.add_parser("add", help="Add a vehicle to the fleet")
    add_parser.add_argument("--type", required=True, choices=["Car", "Bike", "Truck"])
    add_parser.add_argument("--brand", required=True)
    add_parser.add_argument("--year", required=True, type=int)
    add_parser.add_argument("--save", action="store_true", help="Save fleet after adding")

    # drive vehicle
    drive_parser = subparsers.add_parser("drive", help="Drive an existing vehicle")
    drive_parser.add_argument("--brand", required=True)
    drive_parser.add_argument("--km", required=True, type=int)
    drive_parser.add_argument("--save", action="store_true", help="Save fleet after driving")

    # list/report
    subparsers.add_parser("report", help="Show fleet report")

    # save/load
    subparsers.add_parser("save", help="Save fleet to JSON")
    subparsers.add_parser("load", help="Load fleet from JSON")

    return parser


def demo_run(fleet: FleetManager):
    # Demonstration sequence (same as Phase 1)
    car = Car("BMW", 2020)
    bike = Bike("Yamaha", 2019)
    truck = Truck("Volvo", 2021)

    car.drive(50)
    bike.drive(20)
    truck.drive(100)

    fleet.add_vehicle(car)
    fleet.add_vehicle(bike)
    fleet.add_vehicle(truck)

    print("\n--- Fleet Report ----")
    fleet.report()


def main():
    parser = build_parser()
    args = parser.parse_args()
    setup_logging(args.verbose)

    fleet = FleetManager()
    # Attempt to load existing fleet on start (optional)
    fleet.load_fleet("fleet.json")

    if not args.command:
        # No CLI command provided: run demo
        demo_run(fleet)
        return

    if args.command == "add":
        vtype = args.type
        if vtype == "Car":
            vehicle = Car(args.brand, args.year)
        elif vtype == "Bike":
            vehicle = Bike(args.brand, args.year)
        else:
            vehicle = Truck(args.brand, args.year)
        fleet.add_vehicle(vehicle)
        if args.save:
            fleet.save_fleet("fleet.json")
        print("Vehicle added.")
        return

    if args.command == "drive":
        # find vehicle by brand
        target = next((v for v in fleet.vehicles if v.brand == args.brand), None)
        if not target:
            print(f"No vehicle found with brand: {args.brand}")
            return
        target.drive(args.km)
        if args.save:
            fleet.save_fleet("fleet.json")
        print("Drive completed.")
        return

    if args.command == "report":
        print("\n--- Fleet Report ----")
        fleet.report()
        return

    if args.command == "save":
        fleet.save_fleet("fleet.json")
        print("Fleet saved.")
        return

    if args.command == "load":
        fleet.load_fleet("fleet.json")
        print("Fleet loaded.")
        return


if __name__ == "__main__":
    main()

