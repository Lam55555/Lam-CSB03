try: 
    number = float(input("Nhập số: "))
    if number % 2==0:
        print("Số chẵn")
    else:
        print("Số lẻ")
except ValueError:
    print("Phải nhập số")
