def is_int_palindrom(n):
	pldr = str(n)
	return(pldr[::-1] == pldr)
print(is_int_palindrom(111))