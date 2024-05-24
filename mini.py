# p1

# color = ['blue','red','teal','green']
# print('color list: \n',*color)
# addcolor = (input('Input a new color: '))
# color.append(addcolor)
# print(color)

# p2.1

# color = ['blue','red','teal','green']
# print('color list: \n',*color)
# pos = int(input('number of position: '))
# if pos > 0:
#     print(color[pos-1])
# else:
#     print('nhap so lon hon 0')

# p2.2

# color = ['blue','red','teal','green']
# posdel = input('number of position: ')
# if posdel.isdigit()==True:
#     x = int(posdel)
#     # print(type(x))
#     color.pop(x-1)
#     print('new color list:',color)
# else:
#     color.remove(posdel)
#     print('new color list:',color)

# p3.1

# number = [1,3,6,-10,9]
# print([1])
# count = 0
# x = int(input('input a number: '))
# for i in number:
#     if i == x:
#         print(number.index(i)+1)

# p3.2

# number = [1,3,6,-10,9]
# print(sum(number))

# p3.3

# number = []
# print('input the list of numbers.\nEnter 0 to finish')
# while True:
#     n = int(input(''))
#     number.append(n)
#     if n == 0:
#         break
# print(sum(number))

# p4.1

# n = [1,2,3,4,5,6,7,8,10]
# for i in n:
#     # print(i)
#     if i%2==0:
#         print(i,'', end='')

# p4.2

# number = []
# print('input the list of numbers.\nEnter 0 to finish')
# while True:
#     n = int(input(''))
#     if n == 0:
#         break
#     elif n %2==0:
#         number.append(n)
# print(*number)

# p5.1

# q = ['BĐ', 'BTL', 'CG', 'ĐĐ','HBT']
# ds = [247100, 333300, 266800, 420900, 318000]
# for i in ds:
#     if max(ds) == i:
#         print(ds.index(i))
#     if min(ds) == i:
#         print(ds.index(i))

# p8.1

score  = [70,90,76]
inpscore = int(input('input new score: '))
score.append(inpscore)
score.sort(reverse=True)
print(score)
stt  = 0
for i in score:
    stt+=1
    print(stt,':',i)
#  p8.2

score  = [70,90,76,89,70]
inpscore = int(input('input new score: '))
score.append(inpscore)
score.sort(reverse=True)
print(score)
stt  = 0
for i in score:
    stt+=1
    print(stt,':',i)
    if stt ==5:
        break