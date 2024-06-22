from datetime import datetime

f = open('hw/tuan11/dt.txt','a')

a=input('Input a text: ')
while a:
   f.write(datetime.now().strftime("%d/%m/%y %H:%M:%S.%f")+'\n')
   f.write(a+'\n')
   a=input()
   if a == '\n':
      break
f.close()
f = open('hw/tuan11/dt.txt','r')
print(f.read())