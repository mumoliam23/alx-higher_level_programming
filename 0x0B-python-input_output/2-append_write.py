#!/usr/bin/python3
"""Defines a file-appending function."""


def append_write(filename="", text=""):
    """Appends a string to the end of a UTF8 text file.
    Args:
        filename (str): The name of the file to append to.
        text (str): The string to append to the file.
    Returns:
        The number of characters appended.
    """
    with open(filename, "a", encoding="utf-8") as f:
        return f.write(text)

#!/usr/bin/python3
'''  function that reads n lines of a text file (UTF8) and prints it to stdout
'''


def read_lines(filename="", nb_lines=0):
    ''' function: read_lines
    '''
    if filename == "" or type(filename) != str:
        return
    if type(nb_lines) != int:
        return
    counter = 0
    with open(filename, "r") as f:
        for line in f:
            counter += 1
            if nb_lines <= 0 or (counter <= nb_lines and nb_lines > 0):
                print(line, end='')
            else:
                break
