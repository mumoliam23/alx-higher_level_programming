#!/usr/bin/python3
def search_replace(my_list, search, replace):
    #A storage for the new list (inclusive of the searched and replaced occurances)
    new_list = []
    #Iterating over elements of my_list
    for element in my_list:
        if element == search:
            new_list.append(replace)
        else:
            new_list.append(element)
    return new_list
