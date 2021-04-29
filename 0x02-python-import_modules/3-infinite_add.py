#!/usr/bin/python3
import sys
if __name__ == '__main__':
    sys.argv.pop(0)
    sum = 0
    for arg in sys.argv:
        sum += int(arg)
    print(sum)
