def maxProduct( nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    if len(nums)==1:return nums[0]
    p ,f = 1,0
    max_pr = -9999
    for num in nums:
        if num==0:
            p=1
            f=1
            continue
        p *= num
        max_pr = max(p,max_pr)
    p = 1
    for num in nums[::-1]:
        if num==0:
            p=1
            f = 1
            continue
        p *= num
        max_pr = max(p,max_pr)
    if max_pr < 0 and f == 1: return 0
    return max_pr if max_pr >= 1 else -1

  nums = [23,3,-1,0,2,32]
  print(maxProduct(nums))
  # 69 should be the output
  
