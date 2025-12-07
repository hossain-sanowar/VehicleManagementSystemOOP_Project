from VehicleManagementSystemOOP_Project.base import Vehicle

class Truck(Vehicle):
    def drive(self,km):
        self._mileage +=km
        print(f"Truck {self.brand} drove {km} km")
