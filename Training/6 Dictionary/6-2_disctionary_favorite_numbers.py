__author__='dev'
# 6-2. Favorite Numbers: Use a dictionary to store peoples favorite numbers.
# Think of five names, and use them as keys in your dictionary. Think of a favorite
# number for each person, and store each as a value in your dictionary. Print
# each persons name and their favorite number. For even more fun, poll a few
# friends and get some actual data for your program.

people_fav_num = {'Name1': '1', 'Name2': '2', 'Name3': '3', 'Name4': '4'}
# print(person_details['first_name'])
# print(person_details['last_name'])
# print(person_details['age'])
# print(person_details['city'])

# Do it with for or while loop
for i in people_fav_num:
    print (i),"'s " 'favorite number', people_fav_num[i]
