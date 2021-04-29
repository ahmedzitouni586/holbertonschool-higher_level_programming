#!/usr/bin/python3
if __name__ == "__main__":
    from hidden_4 import *
    names = dir(hidden_4)
    for i in names:
        if "__" not in i:
            print(i)
