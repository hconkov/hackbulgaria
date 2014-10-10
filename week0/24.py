def iterations_of_nan_expand(expanded):
	if expanded == '':
		return 0
	elif expanded.count("NaN") != 1:
		return False
	else:
		return(expanded.count("Not a "))
print(iterations_of_nan_expand(""))		
