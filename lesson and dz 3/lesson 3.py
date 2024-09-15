class Human:
    def __init__(self, name = "Human"):
        self.name = name


class Auto:

    def __init__(self, brand):
        self.brand = brand
        self.passengers = []

    def add_passenger(self, *args):
        for passenger in args:
            self.passengers.append(passenger)

    def print_passengers_names(self):
        if self.passengers:
            print(self.brand)
            for passenger in self.passengers:
                print(passenger.name)
        else:
            print(f"No passengers found in {self.brand}")


misha = Human("Misha")
maxim = Human("Max")
jack = Human("Jack")

car = Auto("Dodge Challenger")
car.add_passenger(misha, maxim, jack)

# car.add_passenger(misha)
# car.add_passenger(maxim)
# car.add_passenger(jack)
# car.print_passengers_names()
#
# list_1 = []
# list_2 = [1,2,3]
# print("list 1 =",(bool(list_1)))
# print("list 2 =",(bool(list_2)))
car.print_passengers_names()
