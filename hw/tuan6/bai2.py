import math as m
def snt(x):      #x=11
    if x <2:
        return False
    for i in range(2,int(m.sqrt(x))+1):  # i chay tu 2->can bac 2 cua 11 
        if x % i == 0:          #neu mot so chia het cho phan nguyen cua can bac 2 thi k phai snt
            return False
    return True                 #11/3 !=0 -> la so ngto
number = int(input('Print a number: '))
if snt(number):
    print('la so nguyen to')
else:
    print('khong phai so nguyen to')
