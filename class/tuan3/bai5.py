a = float(input("Nhap so thu nhat: "))
b = float(input("Nhap so thu hai: "))
c = float(input("Nhap so thu ba: "))
 
print("Please enter all 3 numbers")
count = a
numbers = [a, b, c]
for i in numbers:
    if i > count: count = i
print("So lon nhat: ", count)
