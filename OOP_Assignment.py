# activity one
class book:
    def __init__(self,color,model):
        self.color = color
        self.model = model
book1 = book('blue', 'Model 2')
book2 = book('red', 'model 1')

print(book1.color)

# activity two
class Vehicle:
    def move(self):
        pass

class Car(Vehicle):
    def move(self):
        print("Driving")

class Plane(Vehicle):
    def move(self):
        print("Flying")

def vehicle_action(vehicle):
    vehicle.move()

car = Car()
plane = Plane()
vehicle_action(car)
vehicle_action(plane)
