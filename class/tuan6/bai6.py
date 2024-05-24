# mang = []
# so =[]
# def tinhtong():
#     while True:
#         a = input('print a number: ')
#         if a =='ok':
#             break
#         else:
#             mang.append(a)
#     print(mang)
#     for x in mang:
#         if x.isdigit():
#             return print('Dung')
# tinhtong()


mang = []
while True:
    a = input('Input a number: ')
    if a == 'ok':
        break
    else:
        mang.append(a)
so = []
for i in mang:
    if i.isdigit():
        so.append(i)
    print(sum(so))