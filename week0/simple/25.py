def is_prime(n):
    if n < 3:
        return True

    for i in range(2, n - 1):
        if n % i == 0:
            return False
    return True
print(is_prime(125))


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
print(prime_factorization(1000))
