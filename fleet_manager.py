class FleetManager:
    def __init__(self):
        self.vehicles =[]


    def add_vehicle(self, vehicle):
        self.vehicles.append(vehicle)

    def report(self):
        for v in self.vehicles:
            print(f"{v.brand} ({v.year}) - Mileage: {v.mileage}")
