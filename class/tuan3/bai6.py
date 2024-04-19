nam = int(input('nhập năm'))
if nam%100 == 0 & nam % 400==0:
    print('nam này là năm nhuận')
elif (nam%100 !=0) or (nam %4==0):
    print('năm này là năm nhuận')
else:
    print('năm này không phải là năm nhuận')