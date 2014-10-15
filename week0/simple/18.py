def is_decreasing(seq):
    for n in range(0, (len(seq) - 1)):
        if seq[n] < seq[n + 1]:
            return False
    return True
print(is_decreasing([5, 4, 3, 2, 1, 4]))
