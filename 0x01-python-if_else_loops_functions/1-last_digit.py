#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
x = abs(number) % 10
if number < 0:
    x *= -1
if x > 5:
    str = "and is greater than 5"
elif x == 0:
    str = "and is 0"
else:
    str = "and is less than 6 and not 0"
print(f"Last digit of {number} is {x} {str}")
