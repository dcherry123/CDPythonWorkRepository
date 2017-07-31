# 2-6. Famous Quote 2: Repeat Exercise 2-5, but this time store the famous persons
# name in a variable called famous_person. Then compose your message
# and store it in a new variable called message. Print your message.

famous_person = raw_input("Enter the name of the person you admire: ")

message = raw_input("Enter His quote: ")

print ("Your hero {0} once said, {1} ".format(famous_person,message))