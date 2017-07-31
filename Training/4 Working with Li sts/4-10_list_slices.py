# 4-10. Slices: Using one of the programs you wrote in this chapter, add several
# lines to the end of the program that do the following:
#  Print the message, The first three items in the list are:. Then use a slice to
# print the first three items from that programs list.
#  Print the message, Three items from the middle of the list are:. Use a slice
# to print three items from the middle of the list.
#  Print the message, The last three items in the list are:. Use a slice to print
# the last three items in the list.


pizza = ['Pizza1', 'Pizza2', 'Pizza3', 'Pizza4', 'Pizza5', 'Pizza6']

# Print the message, The first three items in the list are:. Then use a slice to
# print the first three items from that programs list.

# Use while loop to print first three items
i = 0
while(i < len(pizza[0:3])):
    print (pizza[i])
    i = i + 1

print("\n")

# Print the message, Three items from the middle of the list are:. Use a slice
# to print three items from the middle of the list.

# Use while loop
i = len(pizza)/2
while(i < len(pizza)):
    print (pizza[i])
    i = i + 1

# print(pizza[1:4])
print("\n")
# Print the message, The last three items in the list are:. Use a slice to print the last three items in the list.

print(pizza[2::])


































