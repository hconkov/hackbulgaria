def groupby(func, seq):
    result = {}
    for element in seq:
        if func(element) in result:
            result[func(element)].append(element)
        else:
            result[func(element)] = []
            result[func(element)].append(element)

    return result

print(groupby(lambda x: 'odd' if x %
              2 else 'even', [1, 2, 3, 5, 8, 9, 10, 12]))
