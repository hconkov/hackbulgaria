def vowels_in_string(n):
	novowels = n.translate(None, 'bBcCdDFfGghHjJKkLlMmNnPpQqRrSstTVvWwXxZz')
	return(len(novowels))
print(vowels_in_string("Theistareykjarbunga"))