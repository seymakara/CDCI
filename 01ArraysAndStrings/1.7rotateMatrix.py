#Matrix is n x n
def rotateMatrix(matrix):
    newArr = [[0]*3 for i in range(3)]

    n = len(matrix)
    for i in range (n):
        for j in range(n):
            newArr[j][n-i-1] = matrix[i][j]
    return newArr

print rotateMatrix([[1,2,3], [4,5,6], [7,8,9]])

#  a       b
#(matrix) (newArr)
# 123 ==> 741
# 456 ==> 852
# 789 ==> 963

# a[0][0] => b[0][2]
# a[0][1] => b[1][2]
# a[0][2] => b[2][2]

# a[0][0] => b[0][2]
# a[0][1] => b[1][2]
# a[0][2] => b[2][2]

