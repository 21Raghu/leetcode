target = 12
position = [10, 8, 0, 5, 3]
speed = [2, 4, 1, 1, 3]
# target = 100
# position = [0,2,4]
# speed = [4,2,1]


arr = sorted(zip(position, speed), reverse=True)
stack = []
sped = (target - arr[0][0]) / arr[0][1]
for pos, sp in arr:
    # print((target - pos) / sp,end=' ')
    stack.append((target - pos) / sp)
    if len(stack) >= 2 and stack[-2] >= stack[-1]:
        stack.pop(0)

print(len(stack))
