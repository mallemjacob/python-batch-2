""" Create a Restaurant class """
""" Attribubtes = restaurant_name, cuisine_type """
""" Methods = describe_restaurant(), open_restaurant() """
""" Make an instance called restaurant from your class. """
""" Access both attributes and call methods. """

class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
    
    def describe_restaurant(self):
        print("The restaurant " + self.restaurant_name + " has " + self.cuisine_type + " cusine type.")
    
    def open_restaurant(self):
        print("The restaurant is open from 6:00 PM to 11:00 PM")
        return False
    
restaurant = Restaurant("Gordon ramsey", "Euro")

print(restaurant.restaurant_name)
print(restaurant.cuisine_type)

restaurant.describe_restaurant()

if restaurant.open_restaurant():
    print("The restaurant is open")
else:
    print("closed")