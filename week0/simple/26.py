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
print(countcoins(8.56))
