# # sum = 0
# a = print('bam Done neu muon dung')
# listNumber = []
# while True:
#     number = float(input('Nhap so: '))
#     if number =='Done':
#         break
#     else:
#         listNumber.append(number)
# print(listNumber)
# # for i in listNumber:
# #     sum+=i
# # print(sum)

# print(sum(listNumber))

input_str = input("Nhap vao cac so cua list: ")
user_list = input_str.split()

for i in range(len(user_list)):
    user_list[i] = int(user_list[i])

def totalNums(x):
    sum = 0
    for i in x:
        sum += i
    return sum

print(totalNums(user_list))