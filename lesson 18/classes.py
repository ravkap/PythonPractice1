class Vehicle:
    def __init__(self, make, model):
        self.make = make
        self.model = model

    def moves(self):
        print("Moves along..")

    def get_make_model(self):
        print(f"I'm a {self.make} {self.model}")


my_car = Vehicle("Toyota", "Rav4")

# print(my_car.make)
# print(my_car.model)
my_car.get_make_model()
my_car.moves()


your_car = Vehicle("Cadillac", "Escalade")
your_car.get_make_model()
your_car.moves()


class Airplane(Vehicle):
    def __init__(self, make, model, faa_id):
        super().__init__(make, model)
        self.faa_id = faa_id

    def moves(self):
        print("Flies Along")

    def get_faa_id(self):
        print(f"My faa identification is {self.faa_id}")


class Truck(Vehicle):
    def moves(self):
        print("Rumbles Along")


class GolfCart(Vehicle):
    pass


cassna = Airplane("Cessna", "Skyhawk", "N-12345")
mack = Truck("Mack", "Pinnacle")
golfwagon = GolfCart("Yamaha", "Gc100")

cassna.get_make_model()
cassna.moves()
cassna.get_faa_id()
mack.get_make_model()
mack.moves()
golfwagon.get_make_model()
golfwagon.moves()

print("")
for v in (my_car, your_car, cassna, golfwagon, mack):
    v.get_make_model()
    v.moves()
