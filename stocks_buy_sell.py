def stock_prize_1(prices):
	mi = mx = prices[0]
	profit = 0
	for prize in arr:
		if prize < mi:
			mi = mx = prize
		mi = min(prize,mi)
		mx = max(prize,mx)
		if profit < (mx-mi):
			profit = mx-mi
        
prices = [7,1,5,3,6,4]  
print(stock_prize_1(prices))
