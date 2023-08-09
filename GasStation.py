

def GasStation(gas, cost):
    if sum(gas) < sum(cost):
        return -1
    g = gas[0]
    re = 0
    tank = 0
    for i in range(len(gas)):
        tank += gas[i] - cost[i]
        if tank < 0:
            tank = 0
            re = i + 1
    return re

#example
gas = [1,2,3,4,5]
cost = [3,4,5,1,2]
print("Index where we should start:",GasStaion(gas,cost))



