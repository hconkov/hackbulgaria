def nan_expand(times):
    key = "NaN"
    if times == 0:
        return 0
    elif times == 1:
        return("Not a NaN")
    elif times > 1:
        key = times*"Not a " + key
    return(key)
print(nan_expand(10))    