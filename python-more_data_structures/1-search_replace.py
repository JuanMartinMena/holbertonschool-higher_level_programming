#!/usr/bin/python3
def search_replace(my_list, search, replace):
    new_list = []
    for i in my_list:
        if i == search:
            # Si se encuentra el elemento a cambiar se remplaza por replace
            new_list.append(replace)
        else:
            # Si el elemento no se encuentra se agrega el que estaba
            new_list.append(i)
    return new_list
