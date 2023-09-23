class Vehicle:
    def __init__(self):
        self.vehicle_type = ""

class Automobile(Vehicle):
    def __init__(self):
        super().__init__()
        self.year = ""
        self.make = ""
        self.model = ""
        self.doors = ""
        self.roof = ""

    def input_car_data(self):
        self.vehicle_type = "car"
        self.year = input("Enter the year: ")
        self.make = input("Enter the make: ")
        self.model = input("Enter the model: ")
        self.doors = input("Enter the number of doors (2 or 4): ")
        self.roof = input("Enter the type of roof (solid or sun roof): ")

    def display_car_data(self):
        print("Vehicle type:", self.vehicle_type)
        print("Year:", self.year)
        print("Make:", self.make)
        print("Model:", self.model)
        print("Number of doors:", self.doors)
        print("Type of roof:", self.roof)

def main():
    car = Automobile()
    car.input_car_data()
    print("\nCar Details:")
    car.display_car_data()

if __name__ == "__main__":
    main()
