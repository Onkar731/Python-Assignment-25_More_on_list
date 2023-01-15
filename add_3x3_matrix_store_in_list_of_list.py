"""
Write a python script to add two matrices each of order 3 x 3.
Store matrix elements in a list of lists.
"""

# creating a 3x3 matrix using list of list
matrix1 = [[1, 2, 3,], [4, 5, 6,], [7, 8, 9,],]
matrix2 = [[1, 2, 3,], [4, 5, 6,], [7, 8, 9,],]

# creating an empty list to store elements
result = list()

# adding two 3x3 matrices and storing it in list of list
i = 0

while i < 3 :
    result.append(list())
    j = 0
    while j < 3 :
        result[i].append(matrix1[i][j] + matrix2[i][j])
        j += 1
    i += 1

# printing result matrix
print("Sum of two 3x3 matrices is", result)