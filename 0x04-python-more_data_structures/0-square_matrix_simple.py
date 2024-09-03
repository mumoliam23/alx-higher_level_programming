#!/usr/bin/python3
def square_matrix_simple(matrix):
     # Create a new matrix to store squared values
     square_matrix = []

     # Iterating through each row in the matrix

     for row in matrix:
         # For each row, square each element and append to a new row
         squared_row = [element * element for element in row]
         square_matrix.append(squared_row)
     return square_matrix
