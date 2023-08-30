#!/usr/bin/python3
def search_replace(my_list, search, replace):
    '''
        A function that traverse through a list for an element that matches
        search and modify it with replace then returns a new list.

        @element: Elements
    '''
    if len(my_list) == 0:
        return my_list

    new_list = [element if element != search else replace for element in my_list]
    return new_list
