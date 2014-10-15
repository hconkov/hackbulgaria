def zodiacs(day, month):

    if (((month == 12) & (day > 21)) | ((month == 1) & (day < 21))):
        return("Capricorn")
    elif (((month == 1) & (day > 20)) | ((month == 2) & (day < 20))):
        return("Aquarius")
    elif (((month == 2) & (day > 19)) | ((month == 3) & (day < 21))):
        return("Pisces")
    elif (((month == 3) & (day > 20)) | ((month == 4) & (day < 20))):
        return("Aries")
    elif (((month == 4) & (day > 20)) | ((month == 5) & (day < 20))):
        return("Taurus")
    elif (((month == 5) & (day > 21)) | ((month == 6) & (day < 22))):
        return("Gemini")
    elif (((month == 6) & (day > 21)) | ((month == 7) & (day < 23))):
        return("Cancer")
    elif (((month == 7) & (day > 22)) | ((month == 8) & (day < 23))):
        return("Leo")
    elif (((month == 8) & (day > 22)) | ((month == 9) & (day < 24))):
        return("Virgo")
    elif (((month == 9) & (day > 23)) | ((month == 10) & (day < 24))):
        return("Libra")
    elif (((month == 10) & (day > 23)) | ((month == 11) & (day < 23))):
        return("Scorpio")
    elif (((month == 11) & (day > 22)) | ((month == 12) & (day < 22))):
        return("Sagittarius")

print(zodiacs(13, 10))
