def split_str(ip, k):
    res = []
    print(len(ip), len(ip)%k)
    if len(ip)%k:
        print(len(ip),ip)
        ip = ip + 'x' * (k-len(ip)%k)
    for i in range(0,len(ip),k):
        res.append(ip[i:k+i])
    return res

s = "abcdefghiok"
k = 3
fill = "x"
print(split_str(s,k))
