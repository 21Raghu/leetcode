def evalRPN(tokens):
    stack = []
    for t in tokens:
        if t not in {"+", "-", "*", "/"}:
            stack.append(int(t))
        else:
            b, a = stack.pop(), stack.pop()
            if t == "+":
                stack.append(a + b)
            elif t == "-":
                stack.append(a - b)
            elif t == "*":
                stack.append(a * b)
            else:
                stack.append(a / b)
    return stack[0]

tok = ["10","6","9","3","+","-11","*","/","*","17","+","5","+"]
print(evalRPN(tok))

