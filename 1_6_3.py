# Task 3
#
# Words combination
#
# Create a program that reads an input string and then creates and prints 5 random strings from characters of the input string.
#
# For example, the program obtained the word ‘hello’, so it should print 5 random strings(words)
# that combine characters ‘h’, ‘e’, ‘l’, ‘l’, ‘o’ -> ‘hlelo’, ‘olelh’, ‘loleh’ …
#
# Tips: Use random module to get random char from string)
import random
from itertools import permutations

a = input('sentence ')
b = list(permutations(a))
i = 0
while i<5:
    print(''.join(b[random.randint(0, len(b))]))
    i+=1
