from VehicleManagementSystemOOP_Project.base import Vehicle

class Bike(Vehicle):
    def drive(self,km):
        self._mileage +=km
        print(f"Bike {self.brand} drove {km} km")
