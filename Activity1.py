# Parent class
class Device:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
    
    def device_info(self):
        return f"{self.brand} {self.model}"

# Child class inheriting from Device
class Smartphone(Device):
    def __init__(self, brand, model, os, storage):
        super().__init__(brand, model)  # inheritance (parent attributes)
        self.os = os
        self.storage = storage
        self.battery = 100  # default value

    def use_app(self, app_name, battery_usage):
        if self.battery - battery_usage >= 0:
            self.battery -= battery_usage
            print(f"Using {app_name}... Battery now at {self.battery}")
        else:
            print(f"Not enough battery to use {app_name}")

    def charge(self):
        self.battery = 100
        print("Battery fully charged!")

# Example usage
phone1 = Smartphone("Apple", "iPhone 15", "iOS", "256GB")
phone2 = Smartphone("Samsung", "Galaxy S25", "Android", "512GB")

print(phone1.device_info())  
phone1.use_app("Instagram", 30)  
phone1.charge()
