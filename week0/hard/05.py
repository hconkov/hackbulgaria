def reduce_file_path(path):
    reduced = path.replace('/./', '/')
    while '//' in reduced:
        reduced = reduced.replace('//', '/')
    if reduced[-1] == '/':
        reduced = reduced[:len(reduced) - 2]
    print reduced
    list1 = reduced.split('/', reduced.count('/'))
    print list1
    for n in list1[1::]:
        if n == '..':
            list1.remove(n)
    if reduced == '':
        return '/'
    else:
        return reduced
print reduce_file_path('///../dadss/dasdsa//dsads////')
