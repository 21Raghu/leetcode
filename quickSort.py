def quicksort(arr):
  if len(arr)<2:
    return arr
  pi = arr[0]
  left = [x for x in arr[1:] if x < pi]
  right = [x for x in arr[1:] if x>= pi]
  return quicksort(left) + pi + quicksort(right)

#driver code
arr = [1,2,3,4,3,23,43,231,12,34]
print(quicksort(arr))
