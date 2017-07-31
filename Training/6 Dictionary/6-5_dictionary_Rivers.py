# 6-5. Rivers: Make a dictionary containing three major rivers and the country
# each river runs through. One key-value pair might be 'nile': 'egypt'.
# Use a loop to print a sentence about each river, such as The Nile runs through Egypt.
# Use a loop to print the name of each river included in the dictionary.
# Use a loop to print the name of each country included in the dictionary.

river_city = {'River1': 'City1', 'River2': 'City2', 'River3': 'City3'}
# print(person_details['first_name'])
# print(person_details['last_name'])
# print(person_details['age'])
# print(person_details['city'])

# Use a loop to print a sentence about each river, such as The Nile runs through Egypt.
for i in river_city:
    print (i),'runs through', river_city[i]

# Use a loop to print the name of each river included in the dictionary.
print " "
for i in river_city:
    print (i)

# Use a loop to print the name of each country included in the dictionary.
print " "
for i in river_city:
    print river_city[i]








