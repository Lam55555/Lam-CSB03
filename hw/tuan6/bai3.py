import math as m
def snt(x):     
    if x <2:
        return False
    for i in range(2,int(m.sqrt(x))+1): 
        if x % i == 0:    
            return False
    return True                
def demsnt(n):
    i = 2  #do so nguyen to bat dau tu 2
    count = 0 #tao bien dem
    while count < n:  #n la du lieu lay tu 'number'
        if snt(i):  #su dung ham ktra snt neu True thi print va tang dem
            print(f"{i} ",end='')
            count+=1
        i+=1
number = int(input('Print a number: '))
demsnt(number)