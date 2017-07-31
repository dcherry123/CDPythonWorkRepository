# 4-11. My Pizzas, Your Pizzas: Start with your program from Exercise 4-1
# (page 60). Make a copy of the list of pizzas, and call it friend_pizzas.
# Then, do the following:
#  Add a new pizza to the original list.
#  Add a different pizza to the list friend_pizzas.
#  Prove that you have two separate lists. Print the message, My favorite
# pizzas are:, and then use a for loop to print the first list. Print the message,
# My friends favorite pizzas are:, and then use a for loop to print the second
# list. Make sure each new pizza is stored in the appropriate list.

pizza = ['Pizza1', 'Pizza2', 'Pizza3', 'Pizza4', 'Pizza5']
print (" ")

# Make a copy of the list of pizzas, and call it friend_pizzas
friend_pizzas = pizza[:]

# Add a new pizza to the original list
pizza.append('Pizza6')
print (" ")
print(pizza)

# Add a different pizza to the list friend_pizzas
print (" ")
friend_pizzas.append('Pizza7')
print(friend_pizzas)


# Prove that you have two separate lists. Print the message, My favorite
# pizzas are:, and then use a for loop to print the first list. Print the message,
# My friends favorite pizzas are:, and then use a for loop to print the second
# list. Make sure each new pizza is stored in the appropriate list.
print (" ")
print('Original Pizza List: {0}, Friends Pizza List: {1} '.format(pizza[:], friend_pizzas[:]))




















