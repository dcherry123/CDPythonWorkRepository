class Restaurant(object):


    def __init__(self, name, cuisine_type):

        self.name = name.title()
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):

        print (self.name + " serves " + self.cuisine_type + "." + "\n")


    def open_restaurant(self):

        print (self.name + " is open now!" + "\n")


# restaurant = Restaurant('Dominos', 'pizza')
# print(restaurant.name)
# print(restaurant.cuisine_type)
#
# restaurant.describe_restaurant()
# restaurant.open_restaurant()

class IceCreamStand(Restaurant):

    def __init__(self, name, cuisine_type):
        # self.name = 'Candy Parlour'
        # self.cuisine_type = 'ice_cream'

        super(IceCreamStand, self).__init__(name, cuisine_type)
        self.flavors = ['Flav1', 'Flav2', 'Flav3']

    def available_flavors(self):
        print("available flavors:" "\n")
        for flavor in self.flavors:
            print("- " + flavor.title())


IceCreamShop = IceCreamStand('Candy Parlour', 'ice_cream')
# IceCreamShop.flavors = ['Flav1', 'Flav2', 'Flav3']

IceCreamShop.describe_restaurant()
IceCreamShop.available_flavors()
