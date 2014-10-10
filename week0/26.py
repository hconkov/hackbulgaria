def calculate_coins(sums):
	coins = [100,50,20,10,5,2,1]
	sums *= 100
	change = {}

	while sums > 0:
		for i in coins:
			if sums - i >=  0:
				if i in change:
					change[i] += 1
				else:
					change[i] = 1
				sums -= i
				break
	return change			
				
print(calculate_coins(0.53))				