# List comprehension exercise
#
# Use a list comprehension to make a list containing tuples (i, j)
# where `i` goes from 1 to 10 and `j` is corresponding to `i` squared.

square = []
for i in range(10):
    t = (i, i**2)
    square.append(t)
print(square)