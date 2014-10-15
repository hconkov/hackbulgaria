def groupby(func, seq):
    print (seq.sort(key=func))
print(groupby(lambda x: x % 2, [0, 1, 2, 3, 4, 5, 6, 7]))
