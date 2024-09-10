#!/usr/bin/python3
def common_elements(set_1, set_2):
    igual = set()
    for i in set_1:
        if i in set_2:
            igual.add(i)
    return igual
