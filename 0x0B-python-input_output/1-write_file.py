#!/usr/bin/python3
"""
A function that writes a string to a text file and returns the numbers of characters written.
"""
def write_file(filename="", text=""):
    with open('filename', 'w') as file_object:
        return file_object.write(text)

''' function that returns the number of lines of a text file
'''

#!/usr/bin/python3
def number_of_lines(filename=""):
    ''' function: number_of_lines
    '''
    if filename == "" or type(filename) != str:
        return 0
    counter = 0
    with open(filename, 'r') as f:
        for line in f:
            counter += 1
    return counter

