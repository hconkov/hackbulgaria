def is_number_balanced(n):
    stringn = str(n)
    length = len(stringn)
    mid = length // 2
    left = 0
    right = 0
    if length % 2 == 0:
        leftp = stringn[:mid]
        rightp = stringn[mid:]
    else:
        leftp = stringn[:mid]
        rightp = stringn[mid + 1:]
    for i in range(0, len(leftp)):
        left += int(leftp[i])
        right += int(rightp[i])
    if left == right:
        return(True)
    else:
        return(False)

print(is_number_balanced(140113))
