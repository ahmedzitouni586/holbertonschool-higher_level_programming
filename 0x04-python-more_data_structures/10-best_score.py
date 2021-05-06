#!/usr/bin/python3
def best_score(a_dictionary):
    best = ""
    m = 0
    if a_dictionary:
        for i, j in a_dictionary.items():
            if j > m:
                best = i
                m = j
        return best
    else:
        return None
