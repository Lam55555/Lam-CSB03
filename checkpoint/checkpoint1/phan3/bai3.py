month = int(input('Input a month: '))
if month == 2:
    print('This month has 28 days')
elif month == 1 and month == 3 and month == 5 and month == 7 and month == 8 and month == 10 and month == 12:
    print('This month has 31 days')
elif month>12:
    print('k co du lieu')
else:
    print('This month has 30 days')