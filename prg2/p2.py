year1 = (input("enter a year YYYY fromat "))
if len(year1)==4 :
    year = int(year1)
    if (year % 400 == 0) and (year % 100 == 0):
     print("{0} is a leap year".format(year))
 
    elif (year % 4 ==0) and (year % 100 != 0):
     print("{0} is a leap year".format(year))

# if not divided by both 400 (century year) and 4 (not century year)
# year is not leap year
    else:
     print("{0} is not a leap year".format(year))
else:
    print(" please enter a year in YYYY format ")