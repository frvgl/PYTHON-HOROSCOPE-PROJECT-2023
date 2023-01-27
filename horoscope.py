date = int(input("Enter your birth date here!: \n"))
if date > 31:
    print("Please enter a valid date of the month. This number should not exceed 31.")
month = input("Enter the month you were born in here! (example: January, February, March etc.: \n")

# Initial birthday input to determine user's astrology sign

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
print("Looks like your Astrology sign is:\n", astrology_sign)

# Find out if the user would like to read their horoscope and continue the program

horoscope_prompt = input("Do you want to see your 2023 horoscope?\n Enter Y to read it\n Enter N to miss out!\n")

if horoscope_prompt == "Y":
    print("Horoscope incoming!\n")
elif horoscope_prompt == "N":
    print("Come back later if curiosity gets the best of you!\n")

# Show user their 2023 horoscope!

if astrology_sign == "Capricorn":
    print("Capricorn 2023 horoscope:\n According to 2023's astrology predictions,\n Capricorn may face some challenges this year when it comes to family relationships. Don't be surprised if you find yourself having more disagreements with a sibling! On a brighter note, it looks like there will be love in the air for you, Capricorn! However, don't hold back from expressing love and true feelings to your partner if you expect the same in return... \n")
elif astrology_sign == "Aquarius":
    print("Aquarius 2023 horoscope:\n According to 2023's astrology predictions,\n Aquarius, it looks like this is your year to shine!\n This is going to be a good year for you in the financial department. You may find some interesting new job opportunities coming your way, and maybe even a shift in careers. Tread carefully as you are advised not to lend money to anyone this year, as the chances of getting your money back don't look too good.\n")
elif astrology_sign == "Pisces":
    print("Pisces 2023 horoscope:\n According to 2023's astrology predictions,\n Pisces will be treated well this year!\n Looks like you might be growing financially this year and getting a lot of support from your parents. Your sibling relationships are improving compared to last year. You might come out of a bad relationship/friendship and take life into your own hands with a positive outlook. Take extra care of you physical and mental health this year and try to become more in tune with your religious/spiritual beliefs. This may bring a lot more positive energy into your life.\n")
elif astrology_sign == "Aries":
    print("Aries 2023 horoscope:\n According to 2023's astrology predictions,\n Aries will have a fortunate year! You are going to fulfill all your dreams this year. You might find yourself more motivated to work on developing your career, personal life, and personality. You might face some struggles in your workplace that could extend to troubles in your personal life. You are advised to create a balance between your personal and professional life to reach some harmony.\n")
elif astrology_sign == "Taurus":
    print("Taurus 2023 horoscope:\n According to 2023's atrology predictions,\n Taurus will have a fruitful year full of success and new beginnings. You may notice a dramatic shift in your career and finances. It could be a good year for promotions and career changes. You will need to stay positive and dedicated, as your finances may require some effort to remain stable. You may feel a spike in happiness and confidence, which might spark a new romance! Remember to be vocal about your expectations in relationships. Looks like an unexpected opportunity overseas may pop up.\n")
elif astrology_sign == "Gemini":
    print("Gemini 2023 horoscope:\n According to 2023's astrology predictions,\n Gemini is being warned to be cautious and avoid impulsive decisions. You may discover that activies you have struggled with in the past will become easier and more enjoyable. This will be a rewarding year for personal development, as long as you do the work! Your communication with important relationships will improve, and your view of your family may shift positively towards a source of inspiration or motivation. Your personal life will only go uphill while you feel a boost in confidence towards your personal abilities and capabilities.\n")
elif astrology_sign == "Cancer":
    print("Cancer 2023 horoscope:\n According to 2023's astrology predictions,\n Cancer may notice a steady uptrend in quality of life! By putting forth your best effort to succeed, you will have a favourable year when it comes to advancing in your career, especially around the third quarter of the year. Opportunities presented may lead to an increase in wealth. This is a good year to set boundaries with your loved ones when it comes to your time and energy. It is a perfect year to plan a celebration with your special someone to show your appreciation and be vulnerable. You may experience physical/mental health problems due to recklessness or avoidance. If you are a student, you may develop a more positive outlook towards your mental and emotional wellbeing.\n")
elif astrology_sign == "Leo":
    print("Leo 2023 horoscope:\n According to 2023's astrology predictions,\n Leo will experience many achievements in their career or field of work this year. By putting forth hard work, you will experience an increase in enthusiasm and self-confidence regarding new opportunities. There will also be work-related travel in your future, along with opportunities to work and exchange ideas with new faces. In terms of relationships, this will be a beneficial year if you take risks and open new doors that may lead to true love. You are advised to stop focusing on past mistakes as well as avoiding aggression. This will protect you from mental and emotional damaging effects.\n")
elif astrology_sign == "Virgo":
    print("Virgo 2023 horoscope:\n According to 2023's astrology predictions,\n Virgo, this is a year of new experiences! Do not accept mediocrity. Be open to new perspectives and take initiative to look for new work. It is a great time to put effort into organizing and decluttering in your home life and workplace. When you are spending money, exercise extreme caution. This is not the year to trust strangers or acquaintences with money and prevent property disputes from getting out of hand. You can make money by traveling this year, as your will be fortunate when it comes to encountering new learning opportunities. Keep up a regular practice when it comes to physical activity and any meditation/calming exercises, as this will bring only improvements regarding your physical and mental health.\n")
elif astrology_sign == "Libra":
    print("Libra 2023 horoscope:\n According to 2023's astrology predictions,\n Libra seems to be facing a lot of luck and positivity this year! You are looking at a positive and happy love life with a possible relationship at the beginning of the year, as well as an increase in the development of your social circle. Libra may experience strong passion and heightened emotions, which will deeply impact their fluctuating relationship with their romantic partner. You are advised exercise patience with this situation. As the year progresses, Jupiter's transition might help you sort out the problems within your relationship.\n")
elif astrology_sign == "Scorpio":
    print("Scorpio 2023 horoscope:\n According to 2023's astrology predictions,\n Scorpio, this is going to be an amazing year for you! You are likely to get an increase in pay in the workplace, and if you are thinking of making an investment this year, it will prove to be profitable. However, excitement due to an increase in pay may translate into an increase in expenses, which may prove troublesome later. You are advised not to engage in any workplace arguments, as this may lead to the downfall or complete loss of your job. You may recieve some good proposals in your personal life and love life as well as your professional life. Tread carefully and this will prove to be a very beneficial year for you, Scorpio\n")
elif astrology_sign == "Saggitarius":
    print("Saggitarius 2023 horoscope:\n According to 2023's astrology predictions,\n Saggitarius, if you maintain your positive outlook, this could be a relatively calm year. It looks like you will be successful in accomplishing your objectives. This could be a great beggining to your career and attract many opportunities. Make sure to pay off any debts to maintain stability in your finances. You will have no trouble dealing with pressures at home, and despite any challenges you will be able to pull through and find happiness in a romantic relationship again. As the year progresses, your network of friends and acquaintences will continue to grow. For students, the first quarter of the year may stall your development. This may result in a negative outlook and feelings of frustration.\n")