def tach():
    chuoi = input('Nhập chuỗi: ').split(',')
    items = [x for x in chuoi]
    items.sort()
    return print(','.join(items))
tach()