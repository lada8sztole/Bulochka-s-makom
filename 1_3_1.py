# Task 1
#
# The greatest number
# Write a Python program to get the largest number from a list of random numbers with the length of 10
# Constraints: use only while loop and random module to generate numbers
# while - не знаем количество элементов, но нам надо остановиться в конкретной точке.
# for - не обязательно знаем, но мы можем пройти от начала до конца список (по кускам или весь)
# numbers = [1, 5, 666, 12, -2, 10000000, 546859, 7, 53333, 0, 4, 0.44, 1234]
import random

# random.seed()
numbers = []
i = 0
while i<10:
    numbers.append(random.randint(0, 666))
    i += 1
print(numbers)
max_number = numbers[0]
i = 0
while i<10:
    if numbers[i] > max_number:
        max_number = numbers[i]
    i += 1
print(max_number)
