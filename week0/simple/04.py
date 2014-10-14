def is_prime(n):
	if n<3:
		return True
	
	for i in range(2,n):
		if n%i==0:
			return False
		else:
			return True	
print(is_prime(1))					
