#maximum subarray

def max_subarray(arr):
	summ = max_sum = 0
	for num in arr:
		summ += num
		if summ < 0:
			summ = 0
		max_sum = max(summ,max_sum)
		
	return (max_sum)

arr = [1,-3,4,-1,2,1,-5,4]
print(max_subarray(arr))
#op 6   i.e [4,-1,2,1]
