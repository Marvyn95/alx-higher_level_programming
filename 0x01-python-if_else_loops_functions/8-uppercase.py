#!/usr/bin/python3
def to_upper(x):
    if ord(x) >= 97 and ord(x) <= 122:
        return (ord(x) - 32)
    else:
        return ord(x)

def uppercase(str):
    nstr = ""
    for i in str:
        nstr = nstr + ("{:c}".format(to_upper(i)))
    print("{:s}".format(nstr))
