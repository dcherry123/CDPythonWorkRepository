# 3-7. Shrinking Guest List: You just found out that your new dinner table wont
# arrive in time for the dinner, and you have space for only two guests.
#  Start with your program from Exercise 3-6. Add a new line that prints a message saying that you can invite only two people for dinner.
#  Use pop() to remove guests from your list one at a time until only two names remain in your list. Each
# time you pop a name from your list, print a message to that person letting them know youre sorry you cant invite them to dinner.
#  Print a message to each of the two people still on your list, letting them know theyre still invited.
#  Use del to remove the last two names from your list, so you have an empty list. Print your list to make sure you
# actually have an empty list at the end of your program.

# Printing first invitee list
invitee_list = ['Dhoni', 'Sachin', 'Ganguly', 'Michael', 'Obama']
# for i in range(0, len(invitee_list)):
#     invitee_list[i] = invitee_list[i].upper()
# i = 0
# while(i < len(invitee_list)):
#     invitee_list[i] = invitee_list[i].upper()
#     print ("List element updated to ", invitee_list[i])
#     i = i + 1
invitee_list = [name.upper() for name in invitee_list]

print("---------FIRST INVITATION LIST-------")
for state in invitee_list:
    state = state.upper()
    print ("Hi " + state + ", today you are invited for dinner!")


# Count and print number of invitee
print("")
number_of_invitee = len(invitee_list)
print ("Total number of invitee : " + str(number_of_invitee))

# Add a new line that prints a message saying that you can invite only two people for dinner
print("")
print ("Oh! I have to curtail the invitee list, lets invite only two person")

# Removing elements from list till 2 are remaining
while(len(invitee_list) > 2):
    popped_invitee = invitee_list.pop(0)
    print("We will miss " + popped_invitee)

# # Remove first guest
# print("")
# popped_invitee = invitee_list.pop(0)
# print("We will miss " + popped_invitee)
#
# # Remove second guest
# print("")
# popped_invitee = invitee_list.pop(0)
# print("We will miss " + popped_invitee)
#
# # Remove third guest
# print("")
# popped_invitee = invitee_list.pop(0)
# print("We will miss " + popped_invitee)

# Remaining two members are still invited
print("")
for state in invitee_list:
    print ("Hi " + state + ", today you are still invited for dinner!")

# Delete remaining two invitees
#del invitee_list[:]
invitee_list = []
#del invitee_list[0]
#del invitee_list[0]
print("")
print("I want to cancel the party, so removing rest two")
print("")
remaining_number_of_invitee = len(invitee_list)
print ("Now total number of remaining invitee : " + str(remaining_number_of_invitee))