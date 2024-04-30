n = int(input('Input a number: '))
s = 0
p = n
while p > 0:
    s += p % 10
    p //= 10
    # n%10
print("Tổng các chữ số của", n,"là",s)