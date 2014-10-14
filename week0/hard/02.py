def unique_words(arr):
    arrs = []
    for i in arr:
        if i not in arrs:
            arrs.append(i)
    return(arrs)
print(unique_words(['python','python','apple']))