# 4-5. Summing a Million: Make a list of the numbers from one to one million,
# and then use min() and max() to make sure your list actually starts at one and
# ends at one million. Also, use the sum() function to see how quickly Python can add a million numbers.
import time

print ("01 Print number using for loops upto one milion" + ".\n")
#numbers =
# int(value) = value

value = list(range(1,10000001))

start = time.clock()
print ("--------------------------------------" + "\n")
print("The minimum number " + str(min(value)) + "\n")
print("The max number " + str(max(value)) + "\n")
print("The sum is " + str(sum(value)) + "\n")

print "Total time = " + str(time.clock() - start)