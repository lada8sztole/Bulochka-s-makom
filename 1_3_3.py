# Extracting numbers.
# Make a list that contains all integers from 1 to 100, then find all integers from the list
# that are divisible by 7 but not a multiple of 5, and store them in a separate list. Finally, print the list.
#
# Constraint: use only while loop for iteration

import random

a = []
i = 0
while i<10:
    a.append(random.randint(1, 100))
    i += 1
b = []
i = 0
while i<10:
    if a[i] % 7 == 0 and a[i] % 5 != 0:
        b.append(a[i])
    i += 1
print(a, b, sep='\n')
