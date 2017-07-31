#
# class Car(object):
#     """A simple attempt to represent a car."""
#
#     def __init__(self, make, model, year):
#         self.make = make
#         self.model = model
#         self.year = year
#         self.odometer_reading = 0
#
#     def get_descriptive_name(self):
#         long_name = str(self.year) + ' ' + self.make + ' ' + self.model
#         return long_name.title()
#
#     def read_odometer(self):
#         print("This car has " + str(self.odometer_reading) + " miles on it.")
#
#     def update_odometer(self, mileage):
#         if mileage >= self.odometer_reading:
#             self.odometer_reading = mileage
#         else:
#             print("You can't roll back an odometer!")
#
#     def increment_odometer(self, miles):
#         self.odometer_reading += miles
#
#
# class ElectricCar(Car):
#     """Represent aspects of a car, specific to electric vehicles."""
#     def __init__(self, make, model, year, battery_size):
#         """Initialize attributes of the parent class.
#         Then initialize attributes specific to an electric car.
#         """
#
#         super(ElectricCar, self).__init__(make, model, year)
#         self.battery_size = battery_size
#
#     def describe_battery(self):
#         """Print a statement describing the battery size."""
#         print("This car has a " + str(self.battery_size) + "-kWh battery.")
#
#
# my_tesla = ElectricCar('tesla', 'model s', 2016, 80)
# print(my_tesla.get_descriptive_name())
# my_tesla.describe_battery()


# print "First module's Name: {}".format(__name__)

# from collections import OrderedDict
#
# favorite_languages = OrderedDict()
#
# favorite_languages['jen'] = 'python'
# favorite_languages['sarah'] = 'c'
# favorite_languages['edward'] = 'ruby'
# favorite_languages['phil'] = 'python'
#
# for name, language in favorite_languages.items():
#     print(name.title() + "'s favorite language is " +
#     language.title() + ".")

from random import randint

class die(object):
    def __init__(self, sides = 6):
        self.sides = sides

    def roll_die(self):
        x = randint(1, self.sides)
        print(str(x))

six = die()
for roll in range(10):
    six.roll_die()










































