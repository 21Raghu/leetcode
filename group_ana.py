strs = ["eat","tea","tan","ate","nat","bat"]
mp = []
d = {}
for st in strs:
    x = ''.join((sorted(st)))
    if x not in d:
        d[x]= [st]
    else:
        d[x] += [st]

for t in  d.values():
    mp.append(t)
print(mp)
