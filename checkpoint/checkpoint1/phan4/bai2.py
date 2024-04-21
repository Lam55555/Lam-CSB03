usn = input('input your username: ')
pw = input('input your password: ')
rppw = input('Repeat password:')
email = input('input your email: ')
if usn == '' or pw == '' or email == '' or rppw =='':
    print('nhap du thong tin')
elif rppw != pw:
    print('Passwords not match. Please input again.')
else:
    print('== Registration ==\nUsername:',usn+'\nPassword:',pw+'\nEmail:',email+'\nRegistered successfully.')