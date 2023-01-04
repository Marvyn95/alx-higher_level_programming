#!/usr/bin/python3
def remove_char_at(str, n):

    new = ""
    k = 0
    for i in str:
        if k != n:
            new = new + i
        k = k + 1
    return new
