def genpar(open,close,s):
    if n*2 == len(s):
        res.append(s)
        return

    if open < n:
        genpar(open+1,close,s+'(')
    if close < open:
        genpar(open,close+1,s+')')
    return res

n = 3
res = []
print(genpar(0,0,''))
