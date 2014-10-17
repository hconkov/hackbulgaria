def reduce_file_path(path):
    indexes = []
    reduced = path.replace('/./', '/')
    while '//' in reduced:
        reduced = reduced.replace('//', '/')
    if reduced[-1] == '/':
        reduced = reduced[:len(reduced) - 2]
    print reduced
    list1 = reduced.split('/')
    for n in range(0, len(list1)-1):
        if list1[n] == '..':
            indexes.append(n)
    for i in indexes:
        list1.remove(list1[i])
        list1.remove(list1[i-1])
    print list1
    for x in list1:
        reduced += x
        print x
    if reduced == '':
        return '/'
    else:
        return reduced

    path_arr = path.split('/')
    print(path_arr.index(''))

print reduce_file_path('//./dasdass/../dasdsas//dsads////')
