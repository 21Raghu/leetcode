m = [[1,1,1],[1,0,1],[1,1,1]]


def set_zeros(m):
    f = 0
    r = c = len(m)
    for i in range(r):
        for j in range(c):
            if m[i][j]==0:
                a = 0
                f = 1
                while a < r:
                    m[i][a] = 0
                    m[a][j] = 0
                    a+=1
                break
        if f==1:break
    print(m)

print(m)
print(set_zeros(m))
