list = []
print('Nhan Done de xac nhan')
while  True: 
    q = str(input('Chọn món ăn bạn muốn: '))
    if q =='Done':
        break
    else:
        list.append(q)
for i in list:
    print(i)
q2 = str(input('Chọn món bạn y/c: '))
print('Bạn chọn món: ',q2)
list.remove(q2)
print('danh sach mon con lai', list)  

