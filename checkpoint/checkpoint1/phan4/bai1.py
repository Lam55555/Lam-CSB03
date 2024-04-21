usn = input('input your username: ')
pw = input('input your password: ')
email = input('input your email: ')
if usn == '' or pw == '' or email == '':
    print('nhap du thong tin')
else:
    print('== Registration ==\nUsername:',usn+'\nPassword:',pw+'\nEmail:',email+'\nRegistered successfully.')