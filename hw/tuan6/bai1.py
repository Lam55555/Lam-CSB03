def is_int(x):
  if x==int(x):
    return True
  else:
    return False

num =float(input("Input number: "))
if is_int(num):
  print(f'{num} is an integer')
else: 
  print(f'{num} is not an integer')