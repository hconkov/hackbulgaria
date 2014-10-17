def memberfibolist(lista, listb, needle):
    listc = []
    while len(listc) < len(needle):
        listc = lista + listb
        lista = listb
        listb = listc
    if needle == listc:
        return True
    else:
        return False
