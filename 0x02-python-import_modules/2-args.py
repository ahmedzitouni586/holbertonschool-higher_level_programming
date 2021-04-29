#!/usr/bin/python3
import sys
if __name__ == "__main__":
    sys.argv.pop(0)
    print(f"{len(sys.argv)} arguments:")
    for i, arg in enumerate(sys.argv):
        print(f"{i}: {arg}")
