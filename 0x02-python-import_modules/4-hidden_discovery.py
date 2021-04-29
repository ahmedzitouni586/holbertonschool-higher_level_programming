#!/usr/bin/python3
from hidden_4 import *
if __name__ == "__main__":
    names = dir(hidden_4)
    for i in names:
        if i.startswith("__" , 0, 2):
            print(i)
