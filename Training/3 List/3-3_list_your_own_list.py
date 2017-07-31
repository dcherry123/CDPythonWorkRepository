# 3-3. Your Own List: Think of your favorite mode of transportation, such as a
# motorcycle or a car, and make a list that stores several examples. Use your list
# to print a series of statements about these items, such as I would like to own a
# Honda motorcycle.

my_favourite_transport_mode = ['I would like to own a Honda motorcycle',
                               'I would like to own a Hero motorcycle',
                               'I would like to own a Active motorcycle',
                               'I would like to own a cycle',
                               'I would like to own a car',
                               'I would like to own a Wego motorcycle'
                               ]

#Converting from lower case to upper case using while loop
i = 0
while(len(my_favourite_transport_mode) > i):
    my_favourite_transport_mode[i] = my_favourite_transport_mode[i].upper()
    i += 1


for name in my_favourite_transport_mode:
    print (name)



# print (my_favourite_transport_mode[0])
# print (my_favourite_transport_mode[1])
# print (my_favourite_transport_mode[2])
# print (my_favourite_transport_mode[3])
# print (my_favourite_transport_mode[4])

# for state in names_list:
#     print("Good morning " + state)

