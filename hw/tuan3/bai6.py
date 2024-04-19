# import array as arr
# import random

a = float(input('nhap so thuc 1: '))
b = float(input('nhap so thuc 2: '))
c = float(input('nhap so thuc 3: '))

# mang = arr.array[a,b,c]
# print(val1)

# mylist = [3.0, 2.0, 1.0]
# print(random.choice(mylist))

if  a < 0 or b<0 or c<0:
    print('vui lòng nhập số dương')
elif a+b>c:
    print('day la canh cua tam giac')    
else:
    print('k phai la canh cua tam giac')

