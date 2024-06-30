import math as m
# #1
# a = int(input('Input first number: '))
# b = int(input('Input second number: '))
# print(f'{a} + {b} = {a+b}')

# #2
# a = float(input("Input a: "))
# b = float(input("Input b: "))
# c = float(input("Input c: "))
# delta = b*b - 4*a*c

# if delta == 0:
#     print("Phương trình có nghiệm kép x1 = x2 =", -b/(2*a))
# if delta > 0:
#     print("Phương trình có 2 nghiệm x1 =", (-b + m.sqrt(delta))/(2*a), " và x2 =", (-b - m.sqrt(delta))/(2*a))
# if delta < 0:
#     print("Phương trình đã cho vô nghiệm ! ")

#3
# def check_palindrome():
#     if string == string[::-1]:
#         return print('Dung')
#     else:
#         return print('sai')

# string = str(input('Input a text: '))
# check_palindrome()

#4
# print('== Welcome to MindX Restaurant ==')
# mang = []
# while True:
#     monan =  input('Please choose a dish: ')
#     if monan in mang:
#         ptrl = input('You choose this already. Anything else?(y/n): ')
#         if ptrl == 'n':
#             break
#     trl = input('Greate choice! Anything else ? (y/n): ')
#     mang.append(monan)
#     if trl == 'n':
#         break
# s = set(mang)
# mangmonan =  list(s)
# print('Well done! Your order:')
# for x in mangmonan:
#     print(f'-{x}')

#5
# dict = {
#     'Iphone12': 28000000,
#     'Samsung N10': 16000000,
#     'Oppo 93': 7500000,
#     'Vsmart': 7400000,
#     'Vivo': 4200000,
# }

# namep = input('Input name of a phone: ')
# if namep in dict:
#     print(f'price of {namep}: {dict[namep]}')

# budget = int(input('Input your budget: '))
# print('Phone that fit your budget')
# for i in dict:
#     if dict[i] < budget:
#         print(f'-{i}: {dict[i]}')

#6
# n = int(input('Input a number: '))
# if n > 0:
#     a =  str(n)
#     print(f'This number has {len(a)} digit(s)')

#7
# def sap_xep_ds_tang(danhSachSo):
#    for i in range(len(danhSachSo)):
#        viTriNhoNhat = i
#        for j in range(i + 1, len(danhSachSo)):
#            if danhSachSo[j] < danhSachSo[viTriNhoNhat]:
#                viTriNhoNhat = j
#        danhSachSo[i], danhSachSo[viTriNhoNhat] = danhSachSo[viTriNhoNhat], danhSachSo[i]
  
# danhSach = input('Input number: ').split()
# danhSachSo = list(map(float, danhSach))
# sap_xep_ds_tang(danhSachSo)
# print(*danhSachSo)

#8
n = int(input("Input a positive number: "))
fib = [0]*(n + 1)
fib[1] = 1
for i in range(2, n + 1):
    fib[i] = fib[i - 1] + fib[i - 2]
print("First",n,"Fibonacci number(s):", *fib[1:])


#aa