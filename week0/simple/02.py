def sum_of_digits(n):
    strs = str(abs(n))
    sums = 0
    for i in strs:
        sums += int(i)
    return(sums)
print(sum_of_digits(-1254))
