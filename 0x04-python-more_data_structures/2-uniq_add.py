#!/usr/bin/python3
def uniq_add(my_list=[]):
    new_list = []
    alll = 0
    for i in my_list:
        if i not in new_list:
            alll = alll + i
            new_list.append(i)
    return alll
