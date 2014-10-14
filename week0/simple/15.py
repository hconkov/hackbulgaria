def list_to_number(digits):
	number = ''
	for i in digits:
		number += str(i)
	return(int(number))
print(list_to_number([1,2,3]))