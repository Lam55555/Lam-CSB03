value = int(input('input a number: '))
if value == 0:
    for i in range(0,value,1):
        print('0')
else:
    for i in range(0,value+1,1):
        print(i)