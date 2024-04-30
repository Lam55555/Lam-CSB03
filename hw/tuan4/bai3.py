n = int(input('Input a number: '))
giaithua = 1
if n >0:
    for i in range(1,n+1):
        giaithua = giaithua*i
        i+=1
    print(n,'!=',giaithua)
elif n == 0:
    print('0!=1')
else:
    print('invalid')