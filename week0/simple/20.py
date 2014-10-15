def sum_matrix(m):
    sum1 = 0
    for n in m:
        sum1 += sum(n)
    return(sum1)
print sum_matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
