from VehicleManagementSystemOOP_Project.fleet_manager import FleetManager
from VehicleManagementSystemOOP_Project.car import Car
from VehicleManagementSystemOOP_Project.bike import Bike
from VehicleManagementSystemOOP_Project.truck import Truck


def test_add_and_report(capsys):
    fleet = FleetManager()
    fleet.add_vehicle(Car("BMW", 2020))
    fleet.add_vehicle(Bike("Yamaha", 2019))
    fleet.add_vehicle(Truck("Volvo", 2021))

    fleet.report()
    captured = capsys.readouterr()
    assert "BMW (2020)" in captured.out
    assert "Yamaha (2019)" in captured.out
    assert "Volvo (2021)" in captured.out


def test_save_and_load(tmp_path):
    fleet = FleetManager()
    c = Car("BMW", 2020); c.drive(10)
    b = Bike("Yamaha", 2019); b.drive(5)
    fleet.add_vehicle(c)
    fleet.add_vehicle(b)

    file = tmp_path / "fleet.json"
    fleet.save_fleet(str(file))

    # Load into a new manager
    fleet2 = FleetManager()
    fleet2.load_fleet(str(file))
    assert len(fleet2.vehicles) == 2
    brands = sorted([v.brand for v in fleet2.vehicles])
    assert brands == ["BMW", "Yamaha"]
    mileages = {v.brand: v.mileage for v in fleet2.vehicles}
    assert mileages["BMW"] == 10
    assert mileages["Yamaha"] == 5

