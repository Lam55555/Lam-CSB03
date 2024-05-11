students = ['Huy','Hieu','Lam','Tai','Khoi']
number = [1,2,3,4,5]
# thêm vào cuối list
students.append('Ngoc')
# thêm sau vị trí 
students.insert(2,'Khoa')
# nối mảng
students.extend(number)
print(students)
# Xóa dựa trên giá trị 
students.remove('Huy')
print(students)
# Xóa dựa trên index
students.pop(1)
print(students)
# Xóa phần tử bằng del 
del students[3]
print(students)

# Xóa hết 
# del students
# students.clear()


# for i in students:
#     print(i)

i = 0
while i < len(students):
    print(students[i])
    i+=1

newList =students + number
print(newList) 

# cách tạo tuple 
myTuples = ('Hieu', 'Lam', 'Ngoc', 'Khoa')
myNumberTuples = tuple((1,5,3,9,0))
myList = list(myTuples)
print(list(myList))