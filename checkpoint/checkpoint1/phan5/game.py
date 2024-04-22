import random
diem = 0
while True:
    diem +=1
    # score = 0
    a = random.randint(-20,20)
    b = random.randint(-20,20)
    operator = ['+','-','*','/']
    opval = random.choice(operator)
    if opval == '+':
        n = a+b
        gacha = random.randint(n-1,n+1)
        print('kq cua', a,'+',b, 'la',gacha)
        kq = int(input('1 = true, 0 = False:  '))
        if kq == 1:
            if gacha == n:
                print('true')
                diem +1
            else:
                print('false')
                break
        else:
            if gacha != n:
                print('true')
                diem +1
            else:
                print('false')
                break
    elif opval == '-':
        n = a-b
        gacha = random.randint(n-1,n+1)
        print('kq cua', a,'-',b, 'la',gacha)
        kq = int(input('1 = true, 0 = False:  '))
        if kq == 1:
            if gacha == n:
                print('true')
                diem +1
                
            else:
                print('false')
                break
        else:
            if gacha != n:
                print('true')
                diem +1
                
            else:
                print('false')
                break
    if opval == '*':
        n = a*b
        gacha = random.randint(n-1,n+1)
        print('kq cua', a,'*',b, 'la',gacha)
        kq = int(input('1 = true, 0 = False:  '))
        if kq == 1:
            if gacha == n:
                print('true')
                diem +1
            else:
                print('false')
                break
        else:
            if gacha != n:
                print('true')
                diem +1
            else:
                print('false')
                break
    if opval == '/':
        while b == 0:
            a = random.randint(-20,20)
            b = random.randint(-20,20)
            n = a/b
            c = int(n)
            gacha = random.randint(c-1,c+1)
            print('kq cua', a,'/',b, 'la',gacha)
            kq = int(input('1 = true, 0 = False:  '))
            if kq == 1:
                if gacha == c:
                    print('true')
                    diem +1
                else:
                    print('false')
            else:
                if gacha != c:
                    print('true')
                    diem +1                    
                else:
                    print('false')
                    break
        else:
            n = a/b
            c = int(n)
            gacha = random.randint(c-1,c+1)
            print('kq cua', a,'/',b, 'la',gacha)
            kq = int(input('1 = true, 0 = False:  '))
            if kq == 1:
                if gacha == c:
                    print('true')
                    diem +1
                else:
                    print('false')
            else:
                if gacha != c:
                    print('true')
                    diem +1                 
                else:
                    print('false')
                    break
print("diem cua ban la",diem-1)
