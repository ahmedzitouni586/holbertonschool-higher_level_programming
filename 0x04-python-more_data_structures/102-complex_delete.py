#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    e = value in a_dictionary.values()
    if e:
        for k, v in a_dictionary.items():
            if value is v:
                del a_dictionary[k]
                break
    return a_dictionary
