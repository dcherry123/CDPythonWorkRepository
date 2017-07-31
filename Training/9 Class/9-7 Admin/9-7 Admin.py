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


# tom = User('tom', 'mat', 'tommat')
# tom.describe_user()
# tom.greet_user()
#
# # peter = User('peter', 'Kunh', 'peterKunh')
# # peter.describe_user()
# # peter.greet_user()
#
# print("\n")
# print("Max number login attempts...")
# tom.increment_login_attempts()
# tom.increment_login_attempts()
# tom.increment_login_attempts()
# tom.increment_login_attempts()
# tom.increment_login_attempts()
# print("  total attempts: " + str(tom.login_attempts))
#
# print("Reset login...")
# tom.reset_login_attempts()
# print("  Login attempts: " + str(tom.login_attempts))


class Admin(User):
    def __init__(self, first_name, last_name, username):
        User.__init__(self, first_name, last_name, username)
        self.privileges = []

    def show_privileges(self):
        print("\nPriviledges")
        for privilege in self.privileges:
            print("- " + privilege)


tom = Admin('tom', 'mat', 'tommat')
tom.describe_user()


tom.privileges = [
    'can reset passwords',
    'can moderate discussions',
    'can suspend accounts',
    ]

tom.show_privileges()



