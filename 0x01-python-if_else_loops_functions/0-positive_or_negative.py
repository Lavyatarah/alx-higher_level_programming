#!/usr/bin/python3
import random
number = random.randint(-10, 10)
#Select a random number and compare the numbers in the range
if number > 0:
    print("{:d} is positive".format(number))

elif number == 0:
    print("{:d} is zero".format(number))

else:
    print("{:d} is negative".format(number))