def find(number,digit):
	nums=str(number)
	digits=str(digit)
	if digits.find(nums) != (-1):
		return True
	else:
		return False

#def contains_digits(number,digits):
	nums=str(number)
	for i in range(0,len(digits)):
		dig=str(digits[i])	
		if dig.find(nums):
			return True
	return False
	

def contains_digits(number,digits):
	for i in range(0,len(digits)):
		dig=str(digits[i])
		if number.count(dig) >= 1:
			return True
		return False	
print(contains_digits(402123, [0, 3, 4,7]))				