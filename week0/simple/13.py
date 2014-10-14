def count_consonants(strs):
	novowels = strs.translate(None, 'aeiouyAEIOUY')
	return(len(novowels))
print(count_consonants("Theistareykjarbunga"))		