def vowels_in_string(n):
    novowels = n.translate(
        None, 'bBcCdDFfGghHjJKkLlMmNnPpQqRrSstTVvWwXxZz !@#$%^&*()_-=1234567890;|,./{}')
    return(len(novowels))
print(vowels_in_string("The istareykjarbunga"))
