def contains_digits(number, digits):
    number = str(number)
    for i in range(0, len(digits)):
        dig = str(digits[i])
        if number.count(dig) >= 1:
            return True
        return False
