#!/usr/bin/python3
import sys
if __name__ == "__main__":
    sys.argv.pop(0)
    if sys.argv == 0:
        print("0 arguments.")
    else:
        print(f"{len(sys.argv)} arguments:")
        for i, arg in enumerate(sys.argv):
            print(f"{i}: {arg}")
