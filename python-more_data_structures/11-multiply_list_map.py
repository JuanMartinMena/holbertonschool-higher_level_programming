#!/usr/bin/python3
def multiply_list_map(my_list=[], number=0):
    # Lambda lo que hace es que define una funcion sin usar def
    # map repite la funcion a cada elemento de la variable
    return list(map(lambda x: x * number, my_list))
