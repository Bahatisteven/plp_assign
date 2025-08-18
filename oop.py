# parent class (general blueprint)
class Smartphone:
    def __init__(self, brand, model, battery=100):
        self.brand = brand          # Attribute
        self.model = model          # Attribute
        self.battery = battery      # Attribute (default: 100%)

    # Method (behavior)
    def call(self, number):
        if self.battery > 0:
            print(f"{self.brand} {self.model} is calling {number}...")
            self.battery -= 10
        else:
            print("Battery too low! Please charge.")

    def charge(self):
        self.battery = 100
        print(f"{self.brand} {self.model} is now fully charged")

# Child class (inherits Smartphone)
class GamingPhone(Smartphone):
    def __init__(self, brand, model, battery=100, cooling_system=True):
        # Inherit from parent
        super().__init__(brand, model, battery)
        self.cooling_system = cooling_system

    # Overriding     def call(self, number):
        print(f"{self.brand} {self.model} (Gaming Edition) is video calling {number}")
        self.battery -= 15

# Create objects
phone1 = Smartphone("Samsung", "Galaxy S23")
phone2 = GamingPhone("Asus", "ROG Phone 6")

# Use methods
phone1.call("0788888888")
phone1.charge()

phone2.call("0799999999")
phone2.charge()
