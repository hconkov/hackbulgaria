def meal(n):
    count = 0

    spam = ''
    while n % 3 != 0:
        n = n // 3
        count += 1
    if n % 5 == 0:
        return(count * 'spam' + 'and eggs')
    else:
        return(count * 'spam')
