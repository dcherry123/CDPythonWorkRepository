# 7-2. Restaurant Seating: Write a program that asks the user how many people
# are in their dinner group. If the answer is more than eight, print a message saying
# theyll have to wait for a table. Otherwise, report that their table is ready.

waiter = raw_input("How many people are in their dinner group? : ")
waiter = int(waiter)


if waiter > 8:
    print("Please wait!")
else:
    print("Please come!")




