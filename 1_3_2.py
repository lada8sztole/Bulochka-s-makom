# Task 2
# Exclusive common numbers.
# Generate 2 lists with the length of 10 with random integers from 1 to 10, and make a third list containing
# the common integers between the 2 initial lists without any duplicates.

# Constraints: use only while loop and random module to generate numbers


import random

a = []
b = []
i = 0
while i<10:
    a.append(random.randint(1, 10))
    b.append(random.randint(1, 10))
    i += 1
# first solution
c = []
i = 0
while i<10:
    if a[i] in b and a[i] not in c:
        c.append(a[i])
    i += 1
print(c)

# second solution
c = list(set(a).intersection(b))
print(c)
