'''Session 2 on 20th July 2017'''

# class Car():
#     """A simple attempt to represent a car."""
#     def __init__(self, make, model, year):
#         """Initialize attributes to describe a car."""
#         self.make = make
#         self.model = model
#         self.year = year
#
#     def get_descriptive_name(self):
#         """Return a neatly formatted descriptive name."""
#         long_name = str(self.year) + ' ' + self.make + ' ' + self.model
#         return long_name
#
# my_new_car = Car('audi', 'a4', 2016)
# print(my_new_car.get_descriptive_name())


















# Change the attribute's value directly

# class Car():
#     def __init__(self, make, model, year):
#         """Initialize attributes to describe a car."""
#         self.make = make
#         self.model = model
#         self.year = year
#         self.odometer_reading = 100
#
#     def get_descriptive_name(self):
#         long_name = str(self.year) + ' ' + self.make + ' ' + self.model
#         return long_name.title()
#
#     def read_odometer(self):
#         """Print a statement showing the car's mileage."""
#         print("This car has " + str(self.odometer_reading) + " miles on it.")
#
# my_new_car = Car('audi', 'a4', 2016)
# print(my_new_car.get_descriptive_name())
# my_new_car.read_odometer()


#   #   #   #   #   #   #   #   #   #   #   #   #   #   #
#                                                       #
#  '''Change the attribute's value through a method'''  #
#                                                       #
#                                                       #
#   #   #   #   #   #   #   #   #   #   #   #   #   #   #

# class Car():
#     def __init__(self, make, model, year):
#         """Initialize attributes to describe a car."""
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
#         """Print a statement showing the car's mileage."""
#         print("This car has " + str(self.odometer_reading) + " miles on it.")
#
#     def update_odometer(self, mileage):
#         """Set the odometer reading to the given value."""
#         self.odometer_reading = mileage
#
#
# my_new_car = Car('audi', 'a4', 2016)
# print(my_new_car.get_descriptive_name())
# # my_new_car.update_odometer(230)
# # my_new_car.read_odometer()
# my_new_car.odometer_reading = 147
# my_new_car.read_odometer()



# '''Incrementing an Attributes Value Through a Method'''
#
# class Car():
#     def __init__(self, make, model, year):
#         """Initialize attributes to describe a car."""
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
#         """Print a statement showing the car's mileage."""
#         print("This car has " + str(self.odometer_reading) + " miles on it.")
#
#     def update_odometer(self, mileage):
#         """Set the odometer reading to the given value."""
#         self.odometer_reading = mileage
#
#     def increment_odometer(self, miles):
#         """Add the given amount to the odometer reading."""
#         self.odometer_reading += miles
#
#
# my_used_car = Car('subaru', 'outback', 2013)
# print(my_used_car.get_descriptive_name())
#
# my_used_car.update_odometer(23500)
# my_used_car.read_odometer()
#
# my_used_car.increment_odometer(100)
# my_used_car.read_odometer()
#
#
#

#   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #
#                                                           #
#            '''Session 3 on 24 July 2017 '''               #
#                                                           #
#   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #


#   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #
#                                                           #
#                '''Defining a child Class'''               #
#                                                           #
#   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #


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
#     def __init__(self, make, model, year):
#         """Initialize attributes of the parent class."""
#         super(ElectricCar, self).__init__(make, model, year)
#
# my_tesla = ElectricCar('tesla', 'model s', 2016)
# print(my_tesla.get_descriptive_name())


#   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #
#                                                           #
# '''Defining Attributes and Methods for the Child Class''' #
#                                                           #
#   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #
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
#     def __init__(self, make, model, year):
#         """Initialize attributes of the parent class.
#         Then initialize attributes specific to an electric car.
#         """
#         super(ElectricCar, self).__init__(make, model, year)
#         self.battery_size = 70
#
#     def describe_battery(self):
#         """Print a statement describing the battery size."""
#         print("This car has a " + str(self.battery_size) + "-kWh battery.")
#
#
# my_tesla = ElectricCar('tesla', 'model s', 2016)
# print(my_tesla.get_descriptive_name())
# my_tesla.describe_battery()


#   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #
#                                                           #
#             '''Instances as Attributes'''                 #
#                                                           #
#   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #

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
# class Battery(object):
#     """A simple attempt to model a battery for an electric car."""
#
#     def __init__(self, battery_size=70):
#         """Initialize the battery's attributes."""
#         self.battery_size = battery_size
#
#     def describe_battery(self):
#         """Print a statement describing the battery size."""
#         print("This car has a " + str(self.battery_size) + "-kWh battery.")
#
#
# class ElectricCar(Car):
#     """ Represent aspects of a car, specific to electric vehicles. """
#     def __init__(self, make, model, year):
#         """Initialize attributes of the parent class.
#         Then initialize attributes specific to an electric car.
#         """
#         super(ElectricCar, self).__init__(make, model, year)
#         self.battery = Battery()
#
#
# my_tesla = ElectricCar('tesla', 'model s', 2016)
# print(my_tesla.get_descriptive_name())
# my_tesla.battery.describe_battery()

#   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #
#                                                           #
#          '''Add another method in Battery Class'''        #
#                                                           #
#   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #

class Car(object):
    """A simple attempt to represent a car."""

    def __init__(self, make, model, year):
        print "CAR CLASS"
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        long_name = str(self.year) + ' ' + self.make + ' ' + self.model
        return long_name.title()

    def read_odometer(self):
        print("This car has " + str(self.odometer_reading) + " miles on it.")

    def update_odometer(self, mileage):
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")

    def increment_odometer(self, miles):
        self.odometer_reading += miles


class Battery(object):
    """A simple attempt to model a battery for an electric car."""

    def __init__(self, battery_size=70):
        """Initialize the battery's attributes."""
        self.battery_size = battery_size

    def describe_battery(self):
        """Print a statement describing the battery size."""
        print("This car has a " + str(self.battery_size) + "-kWh battery.")

    def get_range(self):
        """Print a statement about the range this battery provides."""
        if self.battery_size == 70:
            range = 240
        elif self.battery_size == 85:
            range = 270

        message = "This car can go approximately " + str(range)
        message += " miles on a full charge."
        print(message)


class ElectricCar(Car):
    """ Represent aspects of a car, specific to electric vehicles. """
    def __init__(self, make, model, year):
        """Initialize attributes of the parent class.
        Then initialize attributes specific to an electric car.
        """
        print "ELECTRIC CLASS"
        super(ElectricCar, self).__init__(make, model, year)
        self.battery = Battery()
        print self.battery


my_tesla = ElectricCar('tesla', 'model s', 2016)
print(my_tesla.get_descriptive_name())
my_tesla.battery.describe_battery()
my_tesla.battery.get_range()


#   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #
#                                                           #
#            '''Session 4 on 25 July 2017 '''               #
#                                                           #
#   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #


#   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #
#                                                           #
#                                                           #
#                                                           #
#   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #






















