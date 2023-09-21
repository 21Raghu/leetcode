#tokens = ["2", "1", "+", "3", "*"][::-1]
tokens =["10","6","9","3","+","-11","*","/","*","17","+","5","+"][::-1]
st = []
res = []
op = 0
for ch in tokens:
    if ch in '-+/*':
        st.append(ch)
    elif len(st) > 0:
        op+=1
        res.append('(')
        res.append(ch + st.pop())
    else:
        res.append(ch)
        res.append(')')
        op-=1
print(op)
while op:
    res.append(')')
    op-=1
print(res)
x = "".join(res)
print(x,eval(x))
