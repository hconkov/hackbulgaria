def sevens_in_a_row(arr, n):
    count = 0
    for i in range(0, len(arr)):
        if arr[i] == 7:
            count += 1
            if count >= n:
                return True
        else:
            count = 0
    return False


print(sevens_in_a_row([7, 7, 8, 7], 2))
