def island(mat, i, j):

    if i < 0 or j < 0 or i >= len(mat) or j >= len(mat[0]) or mat[i][j]==0:
        return
    if mat[i][j]==1:
        mat[i][j] = 0

    island(mat, i + 1,  j)
    island(mat, i , j + 1)
    island(mat, i - 1 , j)
    island(mat, i , j - 1)
    island(mat, i - 1 , j - 1)
    island(mat, i + 1 , j + 1)



grid = [[0, 1, 1, 1, 0, 0, 0],
        [0, 0, 1, 1, 0, 1, 0]]

ans = 0
for i in range(len(grid)):
    for j in range(len(grid[0])):
        if grid[i][j] == 1:
            island(grid,i,j)
            print(grid)
            ans += 1


#print(island(grid, 0, 0))
