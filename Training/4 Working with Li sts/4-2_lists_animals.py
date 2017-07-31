# 4-2. Animals: Think of at least three different animals that have a common characteristic.
# Store the names of these animals in a list, and then use a for loop to print out the name of each animal.
# Modify your program to print a statement about each animal, such as A dog would make a great pet.
# Add a line at the end of your program stating what these animals have in common. You could print a sentence such as
# Any of these animals would make a great pet!
animals =['tiger', 'cat', 'lion',]
# for animal in animals:
#     print(animal.upper())

# Convert in to upper case using for loop
# for i in range(0, len(animals)):
#     animals[i] = animals[i].upper()

# Convert in to upper case using while loop
# i = 0
# while(i < len(animals)):
#     animals[i] = animals[i].upper()
#     i = i + 1

# Advance way to convert to upper case
animals = [name.upper() for name in animals]
# Modify your program to print a statement about each animal, such as A dog would make a great pet.

# Store the names of these animals in a list, and then use a for loop to print out the name of each animal.
# Print animals names
print""
print("01 for loop to print out the name of each animal" + ".\n")
for animal_name in animals:
    print(animal_name)
print""
print("---------------------------------------------------------")
print " 02 Modify your program to print a statement about each animal, such as A dog would make a great pet"
# Modify your program to print a statement about each animal, such as A dog would make a great pet.
print""
print (animals[0] + " is a wild animal" "," + animals[1] + " is a domestic animal" " and " + animals[2] + " is a ferocious animal.")

# Add a line at the end of your program stating what these animals have in common. You could print a sentence such as
# Any of these animals would make a great pet!
print("03")
print("All have four legs")






