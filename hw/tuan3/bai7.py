a = float(input('Nhap vao so thuc 1: '))
b = float(input('Nhap vao so thuc 2: '))
c = float(input('Nhap vao so thuc 3: '))

mang = [a,b,c]
if a + b > c and a + c > b and b + c > a:
    if a==b==c:
        print('la tam giac can')
        from turtle import *
        pen()
        backward(a)
        left(60)
        forward(a)
        left(60)
        backward(a)
        right(60)
        mainloop()
    elif a*a+b*b == c*c or a*a+c*c == b*b or c*c+b*b == a*a:
        print('la tam giac vuong')
    else:
        print('la tam giac thuong')
else:
    print('khong phai la tam giac')