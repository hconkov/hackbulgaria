def contains_digit(num, digit):
    nums = str(num)
    digits = str(digit)
    for i in nums:
        if i == digits:
            return True
    return False
print(contains_digit(234516, 7))
