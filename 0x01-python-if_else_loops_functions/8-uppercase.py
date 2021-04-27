#!/usr/bin/python3
def uppercase(str):
    for c in str:
        c = ord(c)
        if c in range(97, 123):
            c -= 32
        print("{0}".format(chr(c)), end='')
    print("")
