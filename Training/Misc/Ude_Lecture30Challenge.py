# Write a small program to ask for a name and an age. When both values have been entered, check if the person
# is the right age to go on an 18-30 holiday (they must be over 18 and under 31). If they are, welcome them to the
# holiday, otherwise print a (polite) message refusing them entry.
name = raw_input("Please enter your name: ")
# name = "Tim"
age = raw_input("How old are you, {0}? ".format(name))
print(age)
print type(age)
age = int(age)
print type(age)
if age >= 18 and age<=30:
    print "You are eligible for the holiday package"
else:
    print("Sorry, you are not eligible")




