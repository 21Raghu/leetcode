count = 0
ar = [1, 2, 3]
def countWays(n):
    if n == 0:
        return 1
    elif n < 0:
        return 0
    return countWays(n - 3) + countWays(n - 2) + countWays(n - 1)

print(countWays(4))
