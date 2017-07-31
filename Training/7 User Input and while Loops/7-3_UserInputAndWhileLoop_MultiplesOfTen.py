# 7-3. Multiples of Ten: Ask the user for a number, and then report whether the
# number is a multiple of 10 or not.

ask_a_number = raw_input("Please enter a number to check whether the number is multiple of 10 oe not: ")
ask_a_number = int(ask_a_number)

if ask_a_number % 10 == 0:
    print("\n" + str(ask_a_number) + " is multiple of 10.")
else:
    print("\n" + str(ask_a_number) + " is NOT multiple of 10.")



