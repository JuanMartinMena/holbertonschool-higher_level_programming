#!/usr/bin/python3
def uniq_add(my_list=[]):
    new_list =[]
    for i in my_list: # recorre my_list
        for j in new_list: # recorre new_list
            if i == j: # Si se encuentra que existe en la nueva lista
                break
            else:
                pass
        new_list.append(i)
    return sum(new_list)
