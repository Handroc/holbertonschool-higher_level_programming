#!/usr/bin/python3
def search_replace(my_list, search, replace):
    replaced_list = my_list.copy()
    for i in range(0, len(replaced_list)):
        if replaced_list[i] == search:
            replaced_list.insert(i, replace)
            replaced_list.remove(search)
    return replaced_list
