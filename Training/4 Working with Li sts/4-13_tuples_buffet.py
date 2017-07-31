# 4-13. Buffet: A buffet-style restaurant offers only five basic foods. Think of five
# simple foods, and store them in a tuple.
#  Use a for loop to print each food the restaurant offers.
#  Try to modify one of the items, and make sure that Python rejects the change.
#  The restaurant changes its menu, replacing two of the items with different foods.
#  Add a block of code that rewrites the tuple, and then use a for loop to print each of the items on the revised menu.

# five simple foods, and store them in a tuple.

basic_food = ('food1', 'food2',  'food3', 'food4', 'food5')
print (basic_food)

# Use a for loop to print each food the restaurant offers.
print(" ")
print("Main Menu: ")
print(" ")

for i in basic_food:
    print(i)

# Try to modify one of the items, and make sure that Python rejects the change

# basic_food[1] = ('changefood')

# The restaurant changes its menu, replacing two of the items with different foods. Add a block of code that rewrites
# the tuple, and then use a for loop to print each of the items on the revised menu.

basic_food = ('food1', 'food2',  'food3', 'food9', 'food10')
print(" ")
print("Revised Menu: ")
print(" ")

for i in basic_food:
    print(i)