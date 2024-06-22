import random as r
n = r.randint(0,999)
dem = 10
while True:
    number = int(input('Input a number: '))
    if number == n:
        print('True')
        break
    else:
        if number > n:
            print(f'{number} lon hon so ngau nhien')
        else:
            print(f'{number} be hon so ngau nhien')
        dem-=1
        print(f"Ban con {dem} lan de chon")
        if dem==0:
            print(n)
            break