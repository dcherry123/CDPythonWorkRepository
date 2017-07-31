# 4-7. Threes: Make a list of the multiples of 3 from 3 to 30. Use a for loop to
# print the numbers in your list.

value = list(range(3, 31, 1))

print ("Three's Table:-")
print ("#" *20 + "\n")

for i in value:
    print (" 3 X " +str(i) + " = " + str(3*i))

