char = {}
chuoi = str(input('Input a text: '))
for i in chuoi:
    if i in char:
        char[i]+=1
    else:
        char[i] = 1
print(char)