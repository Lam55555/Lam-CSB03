try: 
    number = int(input('Nhap vao so nguyen: '))
    print(len(str(number)))
except ValueError:
    print("Phải nhập số nguyen")