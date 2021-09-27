# Using python as a calculator.
# Make a program with 2 numbers saved in separate variables a and b, then print the result for each of the following:
#
# Addition
# Subtraction
# Division
# Multiplication
# Exponent (Power)
# Modulus
# Floor division

a = 10
b = 5
print(a+b)
print(a-b)
print(a*b)
print(a/b)
print(a**b)
print(abs(a), abs(b))
print(a//b)

a = int(input('enter a '))  # a = int(a) - добавить для числового наименования нивелируя строку.
b = int(input('enter b '))  # b = int(b)
print(f'add {a+b}, sub {a-b}, div {a/b}, mult {a*b}, modul {abs(a), abs(b)}, flo {a//b}')
print(f'exp {a**b}')