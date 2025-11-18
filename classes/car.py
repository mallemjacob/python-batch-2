class Car:
    def __init__(self, make, model, year):
        self.maker = make
        self.model_name = model
        self.manufactured_year = year
        self.odometer_reading = 0
        self.places_visited = ['Frace',"Germany","Italy"]

    def read_odometer(self):
        print('The current odometer reading is: ' + str(self.odometer_reading))

    def update_odometer(self, milage):
        if milage > self.odometer_reading:
            self.odometer_reading = milage
        else:
            print('The milage must be greater than the odometer reading!')
    
    def get_places_visited(self):
        for place in self.places_visited:
            print(place)

# creating audi instance
audi = Car('audi', 'A1', 2019)
audi.read_odometer()

# Modifying an Attribute’s Value Directly
audi.odometer_reading = 10
audi.read_odometer()

# Modifying an Attribute’s Value Through a Method
audi.update_odometer(15)
audi.read_odometer()

audi.get_places_visited()
