def is_int_palindrom(n):
    pldr = str(n)
    return(pldr[::-1] == pldr)


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
print next_hack(10)
