#!/usr/bin/python3
"""
A function that writes a string to a text file and returns the numbers of characters written.
"""
def write_file(filename="", text=""):
    with open('filename', 'w') as file_object:
        return file_object.write(text)
