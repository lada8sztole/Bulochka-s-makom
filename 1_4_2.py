# Task 2
#
# The valid phone number program.
#
# Make a program that checks if a string is in the right format for a phone number.
# The program should check that the string contains only numerical characters and is only 10 characters long.
# Print a suitable message depending on the outcome of the string evaluation.

a = input('enter number ')
a = a.strip()
if len(a) == 10 and a.isnumeric():
    print('true')
else:
    print('false')
