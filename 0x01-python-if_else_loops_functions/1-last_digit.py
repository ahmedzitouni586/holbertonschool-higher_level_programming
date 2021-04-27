#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
lastdigit = int(repr(number)[-1])
print("Last digit of {} is {}".format(number, lastdigit))
if lastdigit > 5:
    print("and is greater than 5\n")
elif lastdigit == 0:
    print("and is 0\n")
elif lastdigit < 6 and not 0:
    print("and is less than 6 and not 0\n")