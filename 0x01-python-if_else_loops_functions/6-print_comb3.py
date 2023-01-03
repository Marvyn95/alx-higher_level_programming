#!/usr/bin/python3
for i in range(0, 9):
    p = i + 1
    for j in range(p, 10):
        print("{}{}".format(i, j), end = '\n' if i == 8 and j == 9 else ', ')
