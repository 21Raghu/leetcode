def continer(arr):
    i = 0
    j = len(arr) - 1
    max_val = 0
    while i < j:
        m = min(arr[i],arr[j])
        p =  m * (j-i)
        max_val = max(max_val, p)
        if arr[i] <= arr[j]:
            i+=1
        else:
            j-=1
    return max_val


a = [0,8,0,0,0,0,5,0,10,7]
#    0 1 2 3 4 5 6 7
#a = [1,8,6,2,4,5,4,8,10,7]
#    0 1 2 3 4 5 6 7 8 9
print(continer(a))
