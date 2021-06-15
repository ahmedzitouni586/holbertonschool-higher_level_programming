#!/usr/bin/python3
def weight_average(my_list=[]):
    if not isinstance(my_list, list) or len(my_list) == 0:
        return 0
    avrg = 0
    som = 0
    for couple in my_list:
        avrg += (couple[0] * couple[1])
        som += couple[1]
    return (avrg / som)
