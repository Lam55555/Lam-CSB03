import os
from os import path
a = 'class/tuan11/'+str(input('Input a file name: '))+'.txt'
if path.exists(a):
    # b = open(a,'r')
    with open(a,'r') as f:
        print(f.read())
else:
    print('k co')

os.remove('class/tuan11/names.txt')

# filename = input("Enter a filename: ")

# if os.path.exists(filename):
#     with open(filename, 'r') as f:
#         print(f.read())
# else:
#     print("File not found.")
