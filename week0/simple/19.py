def zero_insert(n):
    numbers = str(n)
    final = ''
    for i in range(len(numbers) - 1):
        if (numbers[i] == numbers[i + 1]) or ((int(numbers[i + 1]) + int(numbers[i])) % 10 == 0):
            final = final + numbers[i] + '0'
        else:
            final = final + numbers[i]
    return(final + numbers[-1])
print(zero_insert(555))
