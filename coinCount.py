def coinCount(ar,tar):
    if tar == 0:
        return 0
    ans = maxsize
    for i in range(len(ar)):

        if tar - ar[i] >= 0:
            subans = coinCount(ar, tar - ar[i])

            if subans + 1 < ans:
                ans = subans + 1

    return ans


target = 18
arr = [1, 5, 7]
dp = [-1] * target
print(coinCount(arr, target,dp))
