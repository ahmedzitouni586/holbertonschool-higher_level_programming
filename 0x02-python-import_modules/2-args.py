#!/usr/bin/python3
import sys
if __name__ == "__main__":
    sys.argv.pop(0)
    if len(sys.argv) == 0:
        print("0 arguments.")
    else:
        if len(sys.argv) == 1:
            print("1 argument:")
            print(f"1: {sys.argv[0]}")
        else:
            print(f"{len(sys.argv)} arguments:")
            for i, arg in enumerate(sys.argv):
                print(f"{i+1}: {arg}")
