usn = input('input your username: ')
pw = input('input your password: ')
rppw = input('Repeat password:')
email = input('input your email: ')
if usn == '' or pw == '' or email == '' or rppw =='':
    print('nhap du thong tin')
elif rppw != pw:
    print('Passwords not match. Please input again.')
elif len(str(pw))<=8:
    print('phai lon hon 8 ky tu')
elif email[len(email)-10:len(email)]!="@gmail.com":
    print('Invalid email. Please input again.')
elif pw.isdigit() == False and pw.isalpha() == False:
    print('== Registration ==\nUsername:',usn+'\nPassword:',pw+'\nEmail:',email+'\nRegistered successfully.')
else:
    print('mk phai co chu lan so')


# # usn = input('input your username: ')
# pw = str(input('input your password: '))
# # rppw = input('Repeat password:')
# email = input('input your email: ')
# # if usn == '' or pw == '' or email == '' or rppw =='':
# #     print('nhap du thong tin')
# # elif rppw != pw:
# #     print('Passwords not match. Please input again.')
# # elif  rppw.isdigit() == True and rppw.isalpha() == True:
# #     print('co chu lan so')
# # elif len(str(pw))<=8:
# #     print('phai lon hon 8 ky tu')
# if email[len(email)-10:len(email)]!="@gmail.com":
#     print('Invalid email. Please input again.')
# elif pw.isdigit() == False and pw.isalpha() == False:
#     # print('== Registration ==\nUsername:',usn+'\nPassword:',pw+'\nEmail:',email+'\nRegistered successfully.')
#     print('True')
# else:
#     print('false')