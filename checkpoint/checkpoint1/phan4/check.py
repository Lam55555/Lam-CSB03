str1 = "333333fghfhfh333";  # chỉ chứa các ký tự chữ và số
if str1.isdigit() == False and str1.isalpha() == False:
    print('dung')
else:
    print('sai')