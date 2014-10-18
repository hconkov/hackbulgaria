def nth_fibonacci(n):
    if n == 1:
        return (1)
    elif n == 2:
        return (1)
    else:
        return(nth_fibonacci(n - 1) + nth_fibonacci(n - 2))


def sum_of_digits(n):
    strs = str(abs(n))
    sums = 0
    for i in strs:
        sums += int(i)
    return(sums)


def sum_of_divisors(n):
    sums = 0
    for i in range(1, n + 1):
        if n % i == 0:
            sums += i
    return(sums)


def is_prime(n):
    if n < 4:
        return True

    for i in range(2, n - 1):
        if n % i == 0:
            return False
    return True


def prime_number_of_divisors(n):
    sums = 0
    for i in range(1, n + 1):
        if n % i == 0:
            sums += 1
    return(is_prime(sums))


def sevens_in_a_row(arr, n):
    count = 0
    for i in range(0, len(arr)):
        if arr[i] == 7:
            count += 1
            if count >= n:
                return True
        else:
            count = 0
    return False


def is_int_palindrom(n):
    pldr = str(n)
    return(pldr[::-1] == pldr)


def contains_digit(num, digit):
    nums = str(num)
    digits = str(digit)
    for i in nums:
        if i == digits:
            return True
    return False


def contains_digits(number, digits):
    number = str(number)
    for i in range(0, len(digits)):
        dig = str(digits[i])
        if number.count(dig) >= 1:
            return True
        return False


def is_number_balanced(n):
    stringn = str(n)
    length = len(stringn)
    mid = length // 2
    left = 0
    right = 0
    if length % 2 == 0:
        leftp = stringn[:mid]
        rightp = stringn[mid:]
    else:
        leftp = stringn[:mid]
        rightp = stringn[mid + 1:]
    for i in range(0, len(leftp)):
        left += int(leftp[i])
        right += int(rightp[i])
    if left == right:
        return(True)
    else:
        return(False)


def count_substrings(haystack, needle):
    return(haystack.count(needle))


def vowels_in_string(n):
    novowels = n.translate(
        None, 'bBcCdDFfGghHjJKkLlMmNnPpQqRrSstTVvWwXxZz !@#$%^&*()_-=1234567890;|,./{}')
    return(len(novowels))


def count_consonants(strs):
    novowels = strs.translate(
        None, 'aeiouyAEIOUY !@#$%^&*()_-=1234567890;|,./{}')
    return(len(novowels))


def number_to_list(n):
    num = str(n)
    diglist = []
    for i in num:
        diglist.append(i)
    return(diglist)


def list_to_number(digits):
    number = ''
    for i in digits:
        number += str(i)
    return(int(number))


def biggest_difference(arr):
    return(min(arr) - max(arr))


def is_increasing(seq):
    for n in range(0, (len(seq) - 1)):
        if seq[n] > seq[n + 1]:
            return False
    return True


def is_decreasing(seq):
    for n in range(0, (len(seq) - 1)):
        if seq[n] < seq[n + 1]:
            return False
    return True


def zero_insert(n):
    numbers = str(n)
    final = ''
    for i in range(len(numbers) - 1):
        if (numbers[i] == numbers[i + 1]) or ((int(numbers[i + 1]) + int(numbers[i])) % 10 == 0):
            final = final + numbers[i] + '0'
        else:
            final = final + numbers[i]
    return(final + numbers[-1])


def sum_matrix(m):
    sum1 = 0
    for n in m:
        sum1 += sum(n)
    return(sum1)
print sum_matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]])


def is_hack(n):
    binary = bin(n)[2:]
    if (binary.count('1') % 2 != 0) & (is_int_palindrom(binary) is True):
        return True
    else:
        return False


def next_hack(n):
    if is_hack(n) is True:
        n += 1
    while is_hack(n) is False:
        n += 1
    return n


def nan_expand(times):
    key = "NaN"
    if times == 0:
        return 0
    elif times == 1:
        return("Not a NaN")
    elif times > 1:
        key = times * "Not a " + key
    return(key)


def iterations_of_nan_expand(expanded):
    if expanded == '':
        return 0
    elif expanded.count("NaN") != 1:
        return False
    else:
        return(expanded.count("Not a "))


def prime_factorization(n):
    list1 = []
    if is_prime(n) is True:
        return (tuple([n, 1]))
    else:
        while is_prime(n) is False:
            for i in range(2, n)[::-1]:
                count = 0
                if (n % i == 0) & (is_prime(i) is True):
                    while n % i == 0:
                        n = n // i
                        count += 1
                    factor = tuple([i, count])
                    list1 += factor
    return(list1)


def countcoins(f):
    coins = [100, 50, 20, 10, 5, 2, 1]
    coinsdict = {'1': 0, '2': 0, '5': 0, '10': 0, '20': 0, '50': 0, '100': 0}
    f = f * 100
    print f
    while f > 0:
        for i in coins:
            if (f - i) >= 0:
                print i
                coinsdict[str(i)] += 1
                f -= i
                break
    return(coinsdict)


def zodiacs(day, month):

    if (((month == 12) & (day > 21)) | ((month == 1) & (day < 21))):
        return("Capricorn")
    elif (((month == 1) & (day > 20)) | ((month == 2) & (day < 20))):
        return("Aquarius")
    elif (((month == 2) & (day > 19)) | ((month == 3) & (day < 21))):
        return("Pisces")
    elif (((month == 3) & (day > 20)) | ((month == 4) & (day < 20))):
        return("Aries")
    elif (((month == 4) & (day > 20)) | ((month == 5) & (day < 20))):
        return("Taurus")
    elif (((month == 5) & (day > 21)) | ((month == 6) & (day < 22))):
        return("Gemini")
    elif (((month == 6) & (day > 21)) | ((month == 7) & (day < 23))):
        return("Cancer")
    elif (((month == 7) & (day > 22)) | ((month == 8) & (day < 23))):
        return("Leo")
    elif (((month == 8) & (day > 22)) | ((month == 9) & (day < 24))):
        return("Virgo")
    elif (((month == 9) & (day > 23)) | ((month == 10) & (day < 24))):
        return("Libra")
    elif (((month == 10) & (day > 23)) | ((month == 11) & (day < 23))):
        return("Scorpio")
    elif (((month == 11) & (day > 22)) | ((month == 12) & (day < 22))):
        return("Sagittarius")
