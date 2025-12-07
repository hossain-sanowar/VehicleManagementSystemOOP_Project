from .base import Vehicle

class Car(Vehicle):
    def drive(self,km):
        self._mileage +=km
        print(f"Car {self.brand} drove {km} km")
