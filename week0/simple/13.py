def count_consonants(strs):
    novowels = strs.translate(
        None, 'aeiouyAEIOUY !@#$%^&*()_-=1234567890;|,./{}')
    return(len(novowels))
print(count_consonants("The istareykjarbunga"))
