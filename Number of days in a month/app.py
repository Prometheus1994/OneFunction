print("Enter the month to know how many days it contains:")
month = input()
if int(month) == 2:
    print("There are 28 days and sometimes 29 days in month {}.".format(month))
    print("Enter the year to know if the month contains 28 days or 29 days:")
    year = input()
    if int(year)%4 == 0:
        print("The year {} is leap so it contains 29 days in month {}.".format(year,month))
    else:
        print("The year {} is not leap so it contains 28 days in month {}.".format(year,month))
else:
    print("There are {} days in month {}.".format(30+((int(month)>7)+int(month)%2)%2,month))
