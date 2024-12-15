class Smartphone:
    def __init__(self, brand, model, battery_capacity, color):
        self.brand = brand
        self.model = model
        self.battery_capacity = battery_capacity
        self.color = color

    def display_info(self):
        print(f"Brand: {self.brand}")
        print(f"Model: {self.model}")
        print(f"Battery Capacity: {self.battery_capacity} mAh")
        print(f"Color: {self.color}")

    def charge(self):
        print(f"{self.brand} {self.model} is charging...")

    def make_call(self, phone_number):
        print(f"Calling {phone_number} from {self.model}...")

my_phone = Smartphone("Apple", "iPhone 14", 4000, "Black")

my_phone.display_info()

my_phone.charge()

my_phone.make_call("+254734536789")

class Vehicle:
    def move(self):
        raise NotImplementedError("Subclasses must implement this method")

class Car(Vehicle):
    def move(self):
        print("Driving 🚗")

class Plane(Vehicle):
    def move(self):
        print("Flying ✈️")

car = Car()
plane = Plane()

car.move()  
plane.move()  
