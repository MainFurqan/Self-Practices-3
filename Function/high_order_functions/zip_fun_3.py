# Q3: Matrix Transpose
# Given a matrix as a list of lists:

# matrix = [
#     [1, 2, 3],
#     [4, 5, 6]
# ]
# Task: Use zip() to transpose the matrix:

# [
#     (1, 4),
#     (2, 5),
#     (3, 6)
# ]

matrix = [
    [1, 2, 3],
    [4, 5, 6]
    ]

result = list(zip(matrix[0], matrix[1]))
print(result)