# 3-6. More Guests: You just found a bigger dinner table, so now more space is
# available. Think of three more guests to invite to dinner.
# Start with your program from Exercise 3-4 or Exercise 3-5. Add a print
# statement to the end of your program informing people that you found a
# bigger dinner table.
# Use insert() to add one new guest to the beginning of your list.
# Use insert() to add one new guest to the middle of your list.
# Use append() to add one new guest to the end of your list.
# Print a new set of invitation messages, one for each person in your list.

# Printing first invitee list
invitee_list = ['Dhoni', 'Sachin', 'Ganguly', 'Michael', 'Obama']

print("---------FIRST INVITATION LIST-------")
for state in invitee_list:

    print ("Hi " + state + ", today you are invited for dinner!")

# Count and print number of invitee
print("")
number_of_invitee = len(invitee_list)

print ("Total number of invitee : " + str(number_of_invitee))

# print message about the availability of bigger table
print("")
print("There is bigger table available, lets invite three more people")

# Use insert() to add one new guest to the beginning of your list

invitee_list.insert(0, 'Gambhir')

# Use insert() to add one new guest to the middle of your list

invitee_list.insert(3, 'Saha')

# Use append() to add one new guest to the end of your list

invitee_list.append('Dhawan')

# Printing updated invitee list
print ""
print("---------NEW INVITATION LIST-------")
for state in invitee_list:

    print ("Hi " + state + ", today you are invited for dinner!")


# Count and print number of invitee
print("")
number_of_invitee = len(invitee_list)
print ("Total number of invitee : " + str(number_of_invitee))