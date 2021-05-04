#!/usr/bin/python3
def max_integer(my_list=[]):
    len_list = len(my_list)
    if (len_list == 0):
        return None
    sorted_list = my_list.sort()
    return sorted_list[-1]
