#!/usr/bin/python3

def best_score(a_dictionary):
    if not isinstance(a_dictionary, dict) or len(a_dictionary) == 0:
        return None

    ret = list(a_dictionary.keys())[0]
    bb = a_dictionary[ret]

    for k, v in a_dictionary.items():
        if v > bb:
            bb = v
            ret = k
    return (ret)
