#!/usr/bin/python3
import sys
if __name__ == '__main__':
    from calculator_1 import add, sub, mul, div
    sys.argv.pop(0)
    if len(sys.argv) != 3:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)
    if sys.argv[1] not in {"+": add, "-": sub, "*": mul, "/": div}:
        print("Unknown operator. Available operators: +, -, * and /\n")
        exit(1)
