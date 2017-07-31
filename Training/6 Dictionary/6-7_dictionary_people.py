# 6-7. People: Start with the program you wrote for Exercise 6-1 (page 102).
# Make two new dictionaries representing different people, and store all three
# dictionaries in a list called people. Loop through your list of people. As you
# loop through the list, print everything you know about each person.

# Make a new dictionaries
People_list1 = {
                'jen': 'I love python',
                'sarah': 'I love c',
                'edward': 'I love ruby',
                'phil': 'I love python',
                }
# Make a new dictionaries
People_list2 = {
                'Aly': 'I love apple',
                'Suji': 'I love orange',
                'Eric': 'I love grapes',
                'Brad': 'I love mango',
                }
# Make a new dictionaries
People_list3 = {
                'Tom': 'I love cycle',
                'Mona': 'I love scooter',
                'Piter': 'I love bus',
                'Kim': 'I love bike',
                }

# store all three dictionaries in a list called people
people = [People_list1, People_list2, People_list3]

# Loop through your list of people
for individual in people:
    print(individual)

