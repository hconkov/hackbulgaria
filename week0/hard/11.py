def is_prime(n):
    if n < 4:
        return True

    for i in range(2, n - 1):
        if n % i == 0:
            return False
    return True


def goldbach(n):
    left = n // 2
    right = n // 2
    list1 = []
    for i in range(1, left):
        tuplist = []
        if (left + right == n) & (is_prime(left) is True) & (is_prime(right) is True):
            tuplist.append(left)
            tuplist.append(right)
            list1.append(tuple(tuplist))
        left -= 1
        right += 1
    return(list1[::-1])
print(goldbach(100))
