class Vehicles:
    def __init__(self):
        print("It is a parent class")

class bus(Vehicles):
    def __init__(self):
        Vehicles.__init__("Bus")

print(issubclass(bus, Vehicles))
print(issubclass(bus, bus))
print(issubclass(bus, list))
