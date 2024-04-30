print("Number with sum of digits = 9")
d = 0
s = 1000
while d<10:
    if sum(int(i) for i in str(s)) == 9:
        print(s,end=' ')
        d+=1
    s+=1
