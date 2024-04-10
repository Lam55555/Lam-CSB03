datedmy  = input("Date in MM/DD/YYYY format: ")
# chia chuoi dua vao dau "/"
mang = datedmy.split("/")
print(f'Date in DD/MM/YYYY format: {mang[1]}/{mang[0]}/{mang[2]}')