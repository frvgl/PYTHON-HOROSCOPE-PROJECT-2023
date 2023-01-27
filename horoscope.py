date = int(input("Input your birth date here!: "))
if date > 31:
    print("Please enter a valid date of the month. This number should not exceed 31.")
month = input("Input the month you were born in here! (example: January, February, March etc.: ")


if month == "January":
    astrology_sign = "Capricorn" if (date < 20) else "Aquarius"
elif month == "February":
    astrology_sign = "Aquarius" if (date < 19) else "Pisces"
elif month == "March":
    astrology_sign = "Pisces" if (date < 21) else "Aries"
elif month == "April":
    astrology_sign = "Aries" if (date < 20) else "Taurus"
elif month == "May":
    astrology_sign = "Taurus" if (date < 21) else "Gemini"
elif month == "June":
    astrology_sign = "Gemini" if (date < 21) else "Cancer"
elif month == "July":
    astrology_sign = "Cancer" if (date < 23) else "Leo"
elif month == "August":
    astrology_sign = "Leo" if (date < 23) else "Virgo"
elif month == "September":
    astrology_sign = "Virgo" if (date < 23) else "Libra"
elif month == "October":
    astrology_sign = "Libra" if (date < 23) else "Scorpio"
elif month == "November":
    astrology_sign = "Scorpio" if (date < 22) else "Saggitarius"
elif month == "December":
    astrology_sign = "Saggitarius" if (date < 22) else "Capricorn"
print("Looks like your Astrology sign is:", astrology_sign)
