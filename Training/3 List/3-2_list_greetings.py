# 3-2. Greetings: Start with the list you used in Exercise 3-1, but instead of just
# printing each persons name, print a message to them. The text of each message
# should be the same, but each message should be personalized with the
# persons name.
names_list = ['peter', 'jack', 'eric']
# print (names_list[0])
# print (names_list[1])
# print (names_list[2])

# Converting from lower case to upper case using for loop
# for i in range(0, len(names_list)):
#     names_list[i] = names_list[i].upper()

# Print the message
# for names in names_list:
#     print("Good morning " + names)

# Converting from lower case to upper case using while loop
# i = 0
# while(len(names_list) > i):
#      names_list[i] = names_list[i].upper()
#      # print ("Name ", names_list[i])
#      i = i + 1

#Print the message
for names in names_list:
    print("Good morning " + names.upper())