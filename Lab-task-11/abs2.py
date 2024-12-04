from abc import ABC, abstractmethod

# Abstract base class representing different types of machines
class Machine(ABC):
    def __init__(self, manufacturer, description):
        self.manufacturer = manufacturer
        self.description = description

    @abstractmethod
    def start_engine(self):
        pass

    def stop_engine(self):
        print(f"The engine of {self.manufacturer} is now off.")

# Concrete class representing a truck
class Truck(Machine):
    def __init__(self, manufacturer, model, description):
        super().__init__(manufacturer, description)
        self.model = model

    def start_engine(self):
        print(f"The engine of {self.manufacturer} {self.model} is starting.")

# Creating an instance of Truck
truck = Truck("Scania", "R500", "Long-haul truck")
truck.start_engine()

# Attempting to instantiate the abstract base class Machine
try:
    machine = Machine("Generic", "Abstract Machine")
except TypeError as error:
    print(f"Error: {error}")
