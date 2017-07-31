# 3-5. Changing Guest List: You just heard that one of your guests cant make the
# dinner, so you need to send out a new set of invitations. Youll have to think of
# someone else to invite.
# - Start with your program from Exercise 3-4. Add a print statement at the
# end of your program stating the name of the guest who cant make it.
# - Modify your list, replacing the name of the guest who cant make it with
# the name of the new person you are inviting.
# - Print a second set of invitation messages, one for each person who is still
# in your list.

# Printing first invitee list
invitee_list = ['Dhoni', 'Sachin', 'Ganguly', 'Michael', 'Obama']

print("---------FIRST INVITATION LIST-------")
for state in invitee_list:

    print ("Hi " + state + ", today you are invited for dinner!")

# Print who is not coming
print ""
print ("Oh! " + (invitee_list[2]) + " could not make it posshible!")

# Add new name in the invitee list
print ""
new_invitee_list = raw_input("Enter the name you want to invite now? ")

# update invitee_list list with new member name
invitee_list[2] = new_invitee_list

# Printing updated invitee list
print ""
print("---------NEW INVITATION LIST-------")
for state in invitee_list:

    print ("Hi " + state + ", today you are invited for dinner!")
