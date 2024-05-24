number = int(input('print a number: '))  
def gthua(x):       #Tinh giai thừa
    gt = 1
    for i in range(1,x+1):
        gt*=i
    return gt
def bieuthuc(n):
    tong = 0
    for i in range(1,n+1):
        tong += gthua(i) / i
    return tong
print(bieuthuc(number))
