f = open('hw/tuan11/text.txt','a')

a=input('Input a text: ')
while a:
   f.write(a+'\n')
   a=input()
   if a == '\n':
      break
f.close()
f = open('hw/tuan11/text.txt','r')
print(f.read())



# def multi_input():
#     try:
#         lst_words = []
#         final_str ='' 
#         print("Please Type in your List of Fruits. \n Press << Enter >> to finish the list:")
        
#         while True:
#             wrd = input()
#             if not wrd: break
#             else:
#                 lst_words.append(wrd)

#     except KeyboardInterrupt:
#         print("program was manually terminated by the user.")
#         return
#     finally:
#         if(len(lst_words)>0):
#             final_str = '\n'.join(lst_words)
#             print('You entered the below fruits:')
#             print(final_str)
#         else:
#             quit
# multi_input()