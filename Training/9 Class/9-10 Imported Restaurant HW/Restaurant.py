class Restaurant():


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