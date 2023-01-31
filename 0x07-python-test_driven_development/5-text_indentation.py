#!/usr/bin/python3

def text_indentation(text):
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    
    lst = []
    for i in range(len(text)):
        lst.append(text[i])

    for i in lst:
        print("{}".format(i), end="")
        if (i == "." or i == "?" or i == ":"):
            print("\n"*2)
