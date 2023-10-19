nums = [1,1,2,5,2,1,0,0,1,3]
def jump_game(nums):
    reachable = 0
    i = 0
    while i < len(nums):
        if reachable < i:
            return False
        reachable = max(reachable,i+nums[i])
        i+=1
    return True

print(jump_game(nums))
