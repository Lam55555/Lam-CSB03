number = int(input('input a number: '))
if number !=0:
    for i in range(0,number+1,1):
        if i %2 !=0:
            print(i)
else:
    print('0')
