#matrix = [[1, 1, 1], [1, 0, 1], [1, 1, 1]]
matrix = [[0, 1, 2, 0], [3, 4, 5, 2], [1, 3, 1, 5]]


def setZeroes(matrix):
    m = len(matrix)
    n = len(matrix[0])

    arr = []
    for i in range(m):
        for j in range(n):
            if matrix[i][j] == 0:
                arr.append([i, j])

    for k, l in arr:
        for row in range(n):
            matrix[k][row] = 0
        for col in range(m):
            matrix[col][l] = 0


setZeroes(matrix)
print(matrix)
