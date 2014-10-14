def is_increasing(seq):
	for n in range(0,(len(seq)-1)):
		if seq[n] > seq[n+1]:
			return False
	return True
print(is_increasing([1,2,3,4,5]))