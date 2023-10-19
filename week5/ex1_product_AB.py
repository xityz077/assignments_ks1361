# Program to multiply two matrices using nested loops

# A: 2x3 matrix
A = [[2,3,4],
     [1,2,3]]

# B: 3x2 matrix
B = [[5,3],
     [6,4],
     [7,5]]

# if (column of A == row of B)
# result matrix has dimension of row of A and column of B
# i.e. 2x2

# result is 3x4
result = [[0,0],
          [0,0]]

# iterate through rows of A
for i in range(len(A)):
    # iterate through columns of B
    for j in range(len(B[0])):
        # iterate through rows of B
        for k in range(len(B)):
            result[i][j] += A[i][k] * B[k][j]


# printing result matrix
for r in result:
    print(r)
