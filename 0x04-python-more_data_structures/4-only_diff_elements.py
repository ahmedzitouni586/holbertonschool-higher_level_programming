#!/usr/bin/python3
def only_diff_elements(set_1, set_2):
    set_3 = set_1.union(set_2)
    set_3.discard("C")
    return set_3
