#   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #
#                                                           #
#          '''Add another method in Battery Class'''        #
#                                                           #
#   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #


#   #   #   #   #   #   #   #   #   #   #   #   #   #   #   ##   #   #   #   #   #   #   #   #
# ''' 9-1. Restaurant: Make a class called Restaurant. The __init__() method for             #
# Restaurant should store two attributes: a restaurant_name and a cuisine_type.              #
# Make a method called describe_restaurant() that prints these two pieces of                 #
# information, and a method called open_restaurant() that prints a message indicating        #
# that the restaurant is open.                                                               #
# Make an instance called restaurant from your class. Print the two attributes               #
# individually, and then call both methods. '''                                              #
#   #   #   #   #   #   #   #   #   #   #   #   #   #   #   ##   #   #   #   #   #   #   #   #

# class Restaurant():
#
#
#     def __init__(self, name, cuisine_type):
#
#         self.name = name.title()
#         self.cuisine_type = cuisine_type
#
#     def describe_restaurant(self):
#
#         print (self.name + " serves " + self.cuisine_type + "." + "\n")
#
#
#     def open_restaurant(self):
#
#         print (self.name + " is open now!" + "\n")
#
#
# restaurant = Restaurant('Dominos', 'pizza')
# print(restaurant.name)
# print(restaurant.cuisine_type)
#
# restaurant.describe_restaurant()
# restaurant.open_restaurant()




#   #   #   #   #   #   #   #   #   #   #   #   #   #   #   ##   #   #   #   #   #   #   #   #
# '''                                                                                         #
#9-2. Three Restaurants: Start with your class from Exercise 9-1. Create three                #
#different instances from the class, and call describe_restaurant() for each                  #
#instance.                                                                                    #
#'''                                                                                          #
#   #   #   #   #   #   #   #   #   #   #   #   #   #   #   ##   #   #   #   #   #   #   #   #


# class Restaurant():
#
#
#     def __init__(self, name, cuisine_type):
#
#         self.name = name.title()
#         self.cuisine_type = cuisine_type
#
#     def describe_restaurant(self):
#
#         print (self.name + " serves " + self.cuisine_type + "." + "\n")
#
#
#     def open_restaurant(self):
#         print (self.name + " is open now!" + "\n")
#
#
# dominos = Restaurant('Dominos', 'pizza')
# dominos.describe_restaurant()
#
# dominos.open_restaurant()
#
# italian = Restaurant("Italian", 'Cheese')
# italian.describe_restaurant()
#
#
# chinese = Restaurant('chinese', 'noodles')
# chinese.describe_restaurant()


#   #   #   #   #   #   #   #   #   #   #   #   #   #   #   ##   #   #   #   #   #   #   #  #
# '''9-3. Users: Make a class called User. Create two attributes called first_name          #
# and last_name, and then create several other attributes that are typically stored         #
# in a user profile. Make a method called describe_user() that prints a summary             #
# of the user's information. Make another method called greet_user() that prints            #
# a personalized greeting to the user.                                                      #
# Create several instances representing different users, and call both methods              #
# for each user.                                                                            #
# #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   ##   #   #   #   #   #   #    #


#   #   #   #   #   #   #   #   #   #   #   #   #   #   #   ##   #   #   #   #   #   #   #   #
#                                                                                            #
#                                       Session 2 Home Work                                  #
#                                                                                            #
#   #   #   #   #   #   #   #   #   #   #   #   #   #   #   ##   #   #   #   #   #   #   #   #




#   #   #   #   #   #   #   #   #   #   #   #   #   #   #   ##   #   #   #   #   #   #   #   #
# Session 2 Home Work                                                                        #
# 9-4. Number Served: Start with your program from Exercise 9-1 (page 166).                  #
# Add an attribute called number_served with a default value of 0. Create an                 #
# instance called restaurant from this class. Print the number of customers the              #
# restaurant has served, and then change this value and print it again.                      #
# Add a method called set_number_served() that lets you set the number                       #
# of customers that have been served. Call this method with a new number and                 #
# print the value again.                                                                     #
# Add a method called increment_number_served() that lets you increment                      #
# the number of customers whove been served. Call this method with any number                #
# you like that could represent how many customers were served in, say, a                    #
# day of business.                                 #                                         #
#   #   #   #   #   #   #   #   #   #   #   #   #   #   #   ##   #   #   #   #   #   #   #   #


# class Restaurant():
#
#     def __init__(self, name, cuisine_type):
#         self.name = name.title()
#         self.cuisine_type = cuisine_type
#         self.number_served = 0
#
#     def describe_restaurant(self):
#         print (self.name + " serves " + self.cuisine_type + "." + "\n")
#
#     def open_restaurant(self):
#         print (self.name + " is open now!" + "\n")
#
#     def set_number_served(self, number_served):
#         self.number_served = number_served
#
#     def increment_number_served(self, increement_cust_served):
#         self.number_served += increement_cust_served
#
#
# restaurant = Restaurant('Dominos', 'pizza')
# restaurant.describe_restaurant()
#
#
# print("\n")
# print("Number or service: " + str(restaurant.number_served))
# restaurant.number_served = 100
# print("Number or service: " + str(restaurant.number_served))
#
# restaurant.set_number_served(150)
# print("Number or service: " + str(restaurant.number_served))
#
# restaurant.increment_number_served(200)
# print("Number or service: " + str(restaurant.number_served))


#   #   #   #   #   #   #   #   #   #   #   #   #   #   #   ##   #   #   #   #   #   #   #   #
# 9-5. Login Attempts: Add an attribute called login_attempts to your User                   #
# class from Exercise 9-3 (page 166). Write a method called increment_                       #
# login_attempts() that increments the value of login_attempts by 1. Write                   #
# another method called reset_login_attempts() that resets the value of login_               #
# attempts to 0.                                                                             #
# Make an instance of the User class and call increment_login_attempts()                     #
# several times. Print the value of login_attempts to make sure it was incremented           #
# properly, and then call reset_login_attempts(). Print login_attempts again to              #
# make sure it was reset to 0.                                                               #
#   #   #   #   #   #   #   #   #   #   #   #   #   #   #   ##   #   #   #   #   #   #   #   #

class User():


    def __init__(self, first_name, last_name, username):
        self.first_name = first_name.title()
        self.last_name = last_name.title()
        self.username = username
        self.login_attempts = 0

    def describe_user(self):
        print("\n" + self.first_name + " " + self.last_name)

    def greet_user(self):
       print("\nWelcome back, " + self.username)

    def increment_login_attempts(self):
        self.login_attempts += 1

    def reset_login_attempts(self):
        self.login_attempts = 0


tom = User('tom', 'mat', 'tommat')
tom.describe_user()
tom.greet_user()

# peter = User('peter', 'Kunh', 'peterKunh')
# peter.describe_user()
# peter.greet_user()

print("\n")
print("Max number login attempts...")
tom.increment_login_attempts()
tom.increment_login_attempts()
tom.increment_login_attempts()
tom.increment_login_attempts()
tom.increment_login_attempts()
print("  total attempts: " + str(tom.login_attempts))

print("Reset login...")
tom.reset_login_attempts()
print("  Login attempts: " + str(tom.login_attempts))









