#!/usr/bin/python3
str = "Python is an interpreted, interactive, object-oriented programming\
       language that combines remarkable power with very clear syntax"
str = ' '.join(str.split()[5:7] + str.split()[12:13] + str.split()[0:1])
print(str)
