pc = {
    'HP': 20,
    'DELL': 50,
    'MACBOOK': 12,
    'ASUS': 30,
}

print('Số lượng Macbook có trong kho là',pc['MACBOOK'])
name = input('Nhap ten may: ')
print(f"Số lượng máy {name} còn lại là",pc[name])