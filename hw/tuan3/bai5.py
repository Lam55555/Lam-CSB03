username = 'admin'
password = '12345'
inuser = input('Username: ')
inpass = input('Password: ')
if inuser == username and inpass==password:
    print('You are logged in, admin.')
else:
    print('Wrong username or password.')