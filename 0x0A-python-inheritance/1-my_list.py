#!/usr/bin/python3

"""Module:1-my_list
"""

class MyList(list):
    """Child class"""

    def print_sorted(self):
        """
        Prints sorted list
        """
        print(sorted(self))
