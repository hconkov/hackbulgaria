def fibolist(lista, listb, n):
    listc = []
    if n == 1:
        return (lista)
    elif n == 2:
        return (listb)
    else:
        for i in range(3, n + 1):
            listc = lista + listb
            lista = listb
            listb = listc
    return(listc)
print(fibolist([1, 2], [1, 3], 3))
