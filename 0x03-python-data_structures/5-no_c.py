#!/usr/bin/python3
def no_c(my_string):
    char = ['C', 'c']
    my_string = ''.join((filter(lambda i: i not in char, my_string)))
    return my_string
