def countwords(arr1):
	dict = {}
	for i in arr1:
		dict[i] = arr1.count(i)
	return(dict)
print(countwords(["apple","apple","green","red", "red","red"]))