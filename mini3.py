#p1.1

# number = float(input('Input a number: '))
# def chanle(x):
#     if x % 2 ==0:
#         return True
#     else:
#         return False
# if chanle(number):
#     print('This number is even')
# else:
#     print('This number is not even')

# p1.2

# def cal_area():
#     r = float(input('Input radius: '))
#     ca = r*3.14
#     return ca
# print("Cirlce's area:",cal_area())

# p1.3

# def reverse_str():
#     string = input('Print a text: ')
#     a = ''.join(reversed(string))
#     return a
# print('Reversed text:', reverse_str())

# p1.4

# def isPalindrome():
#     text = input('Input a text: ')
#     if text == text[::-1]:
#         return True
#     else:
#         return False
 
# if isPalindrome():
#     print("This is a palindrome")
# else:
#     print("This is not a palindrome")

# p2.1

# number = int(input('print a number: '))  
# def gthua(x):       #Tinh giai thừa
#     gt = 1
#     for i in range(1,x+1):
#         gt*=i
#     return gt
# print(f'{number}!=',gthua(number))

# p2.2

# def sap_xep_ds_tang(danhSachSo):
#    for i in range(len(danhSachSo)):
#        #Luu vi tri nho nhat
#        viTriNhoNhat = i
#        for j in range(i + 1, len(danhSachSo)):
#            if danhSachSo[j] < danhSachSo[viTriNhoNhat]:
#                viTriNhoNhat = j
#        danhSachSo[i], danhSachSo[viTriNhoNhat] = danhSachSo[viTriNhoNhat], danhSachSo[i]
  
# danhSach = input().split()
# if len(danhSach) == 0:
#    print("Danh sach rong")
# else:
#     danhSachSo = list(map(float, danhSach))
#     sap_xep_ds_tang(danhSachSo)
#     print(*danhSachSo)

# p2.3

# def fibonacci(n):
#    if n <= 1:
#        return 1
#    else:
#        return(n-1) + (n-2)

# number = int(input("Input a number: "))
# print("Fibonacci:")
# for i in range(number):
#     print(fibonacci(i), end=', ')

# p3.1

# number = int(input('Input a number: '))
# def hieu(x):
#     a = x-17
#     if x - 17 > 17:
#         return a*2
#     elif a < 0:
#         return -a
#     return False
# print(hieu(number))


# p3.3
# list_num = [1,2,3,4,5,6,7,8,4,5,6,3,2,1,4,5,6,4,4,4,4,4]
# def dem():
#     return list_num.count(4)
# print(dem())

# p3.4

# def danh_sach_so_le(danhSachSo):

#    danhSachSoLe = []
#    for so in danhSachSo:
#         if so % 2 == 0:
#            danhSachSoLe.append(so)
#         if so == 237: 
#            break
#    return danhSachSoLe

# numbers = [386, 462, 47, 418, 907, 344, 236, 375, 823, 566, 597, 978, 328, 615, 953, 345, 
# 399, 162, 758, 219, 918, 237, 412, 566, 826, 248, 866, 950, 626, 949, 687, 217, 
# 815, 67, 104, 58, 512, 24, 892, 894, 767, 553, 81, 379, 843, 831, 445, 742, 717, 958,743, 527
# ]


# danhSachSo = list(map(int, numbers))
# dsSoLe = danh_sach_so_le(danhSachSo)
# print(*dsSoLe)