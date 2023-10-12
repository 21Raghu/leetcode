#backtrack
#letter combination
digits = "23"
n = len(digits)
def letter_com(digits):
    n = len(digits)
    if n == 0:
        return []
    dic = {'2': ['a', 'b', 'c'], '3': ['d', 'e', 'f'], '4': ['g', 'h', 'i'], '5': ['j', 'k', 'l'], '6': ['m', 'n', 'o'],
           '7': ['p', 'q', 'r', 's'], '8': ['t', 'u', 'v'], '9': ['w', 'x', 'y', 'z']}
    res = []

    def backtracking(r):
        if len(r) == n:
            res.append(r)
        else:
            for i in dic[digits[len(r)]]:
                backtracking(r + i)

    backtracking("")
    return res
print(letter_com(digits))
