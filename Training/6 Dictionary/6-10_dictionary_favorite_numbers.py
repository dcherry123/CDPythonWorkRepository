# 6-10. Favorite Numbers: Modify your program from Exercise 6-2 (page 102) so
# each person can have more than one favorite number. Then print each persons
# name along with their favorite numbers.

people_fav_num = {
                  'Name1': ['11' ' ' '12' ' ' '13'],
                  'Name2': ['21' ' ' '22' ' ' '23'],
                  'Name3': ['31' ' ' '32' ' ' '33'],
                  'Name4': ['41' ' ' '42' ' ' '43']
                 }
# print(person_details['first_name'])
# print(person_details['last_name'])
# print(person_details['age'])
# print(person_details['city'])

# Do it with for or while loop
for name, numbers in sorted(people_fav_num.items()):
    print("\n" + name.title() + "'s favourite numbers are: ")
    for number in numbers:
        print(" " + str(number))