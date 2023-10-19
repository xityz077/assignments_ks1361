# Given matrices R,S, T
# Program to find 2RS - 3ST

# R: 3x3 matrix
R = [[1,0,2],
     [2,1,5],
     [2,3,1]]

# S: 3x3 matrix
S = [[0,-1,2],
     [3,1,0],
     [4,2,1]]

# T: 3x3 matrix
T = [[-2,3,0],
     [-3,2,2],
     [-1,1,0]]

# RS is 3x3
RS = [[0,0,0],
      [0,0,0],
      [0,0,0]]

# ST is 3x3
ST = [[0,0,0],
      [0,0,0],
      [0,0,0]]

# result is 3x3
result = [[0,0,0],
          [0,0,0],
          [0,0,0]]

# Product of RS
# iterate through rows of A
for i in range(len(R)):
    # iterate through columns of B
    for j in range(len(S[0])):
        # iterate through rows of B
        for k in range(len(S)):
            RS[i][j] += R[i][k] * S[k][j]
# [[8, 3,4],
#  [23,9,9],
#  [13,3,5]]

# Product of ST
# iterate through rows of A
for i in range(len(S)):
    # iterate through columns of B
    for j in range(len(T[0])):
        # iterate through rows of B
        for k in range(len(T)):
            ST[i][j] += S[i][k] * T[k][j]
# [[1, 0, -2],
#  [-9,11,2],
#  [15,17,4]]

# 2RS - 3ST
# iterate through rows of A
for i in range(len(RS)):
    # iterate through columns of B
    for j in range(len(RS[0])):
        result[i][j] = 2*(RS[i][j]) - 3*(ST[i][j])

# printing result matrix
for r in result:
    print(r)
