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

# Inheritance
# Parent --> Child
# Inherit attributes and methods for parent class


class Battery:
    def __init__(self, battery_size, voltage, capacity, energy_density, power_output):
        self.battery_size = battery_size
        self.voltage = voltage
        self.capacity = capacity
        self.energy_density = energy_density
        self.power_output = power_output
    
    def set_charge_cycles(self, c, v):
        self.capacity = c
        self.voltage = v
        return "Charge cycles: " + str(self.capacity * self.voltage)

    def durability_and_lifespan(self):
        return "Durability and lifespan"
    

# b1 = Battery()

class ElectricCar(Car):
    def __init__(self, make, model, year, a, b, c, d, e):
        super().__init__(make, model, year)
        self.battery_details = Battery(a,b,c,d,e)
        
    # def get_battery_size(self):
    #     return self.battery_size
    
    def read_odometer(self):
        return "This is odometer reading from electric class"


ec1 = ElectricCar('tesla','A1',2026, 10,20,30,40,50)
ec2 = ElectricCar('bmw','Z1', 2027,110,120,130,140,150)

print("ec1 model name: " + ec1.model_name)
ec1.get_places_visited()

# print(str(ec1.battery_size) + " kw")

# print(ec1.get_battery_size())

print(ec1.read_odometer())

print(ec1.battery_details.set_charge_cycles(10,20))
# ec1.battery_details.energy_density = 50
print(ec1.battery_details.energy_density)

print(ec2.battery_details.voltage)
print(ec2.battery_details.capacity)

# Composition
# Create a Engine class and use its instance as attribute in the ElectricCar class attribute.

# Inheritance
# Create a ElectricSportCar class from ElectricCar class.
# Add its own attributes and methods.
# Create instances from it.