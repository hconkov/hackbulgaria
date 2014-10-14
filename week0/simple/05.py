def is_prime(n):
	if n<3:
		return True
	
	for i in range(2,n):
		if n%i==0:
			return False
		else:
			return True	

def prime_number_of_divisors(n):
	sums=0
	for i in range(1,n+1):
		if n%i==0:
			sums+=1
	return(is_prime(sums))

print(prime_number_of_divisors(20)) 	