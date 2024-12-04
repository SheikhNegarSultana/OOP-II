from abc import ABC, abstractmethod

# Abstract base class representing a general machine
class Machine(ABC):
    @abstractmethod
    def power_on(self):
        pass

    @abstractmethod
    def power_off(self):
        pass

# Concrete class representing a car
class Coupe(Machine):
    def __init__(self):
        pass

    def power_on(self):
        print("Coupe's engine is now running.")

    def power_off(self):
        print("Coupe has stopped.")

# Concrete class representing a motorbike
class Cruiser(Machine):
    def __init__(self):
        pass

    def power_on(self):
        print("Cruiser bike's engine has started.")

    def power_off(self):
        print("Cruiser bike has halted.")

# Creating instances of Coupe and Cruiser
coupe = Coupe()
coupe.power_on()

# Attempting to instantiate the abstract base class Machine
try:
    machine = Machine()  # Will raise an error since Machine is abstract
except TypeError as exception:
    print(f"Error encountered: {exception}")
