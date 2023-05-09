def three_sum(nums):
    nums = sorted(nums)
    k = len(nums) - 1
    res = set()
    for i in range(len(nums)):
        j = i+1
        while j < k:
            if nums[i]+nums[j]+nums[k]==0:
                l = (nums[i],nums[j],nums[k])
                res.add(l)
                j+=1
                k-=1
            elif nums[j] < nums[k]:
                j+=1
            else:
                k-=1
    return res
 
#this is only solving few testcases might need some more inputs here

a= [-1,0,1,2,-1,-4]
print(three_sum(a))
