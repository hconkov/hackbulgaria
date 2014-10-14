def fractions(fraction):
    fractions = list(fraction)
    for n in range(2, min(fractions) + 1)[::-1]:
        if (fractions[0] % n == 0) & (fractions[1] % n == 0):
            fractions[0] = fractions[0] // n
            fractions[1] = fractions[1] // n
    return(tuple(fractions))
