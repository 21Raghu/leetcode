def rotate(self, matrix: List[List[int]]) -> None:
    i = len(matrix) - 1
    j = 0
    while j < i:
        matrix[i],matrix[j] = matrix[j],matrix[i]
        i-=1
        j+=1

    for i in range(len(matrix)):
        for j in range(i+1,len(matrix)): 
            matrix[i][j],matrix[j][i] = matrix[j][i], matrix[i][j]
    
    return matrix

mat = [[1, 2, 3],
	[4, 5, 6],
	[7, 8, 9]]
rotateMatrix(mat)
