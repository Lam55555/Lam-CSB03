usn = input('input your username: ')
pw = input('input your password: ')
rppw = input('Repeat password:')
email = input('input your email: ')
if usn == '' or pw == '' or email == '' or rppw =='':
    print('nhap du thong tin')
elif len(str(pw))<8 and pw.isdigit() == False and pw.isalpha() == False:
    print('phai lon hon 8 ky tu va phai co chu lan so')
elif rppw != pw:
    print('Passwords not match. Please input again.')
elif email[len(email)-10:len(email)]!="@gmail.com":
    print('Invalid email. Please input again.')
else:
    print('== Registration ==\nUsername:',usn+'\nPassword:',pw+'\nEmail:',email+'\nRegistered successfully.')