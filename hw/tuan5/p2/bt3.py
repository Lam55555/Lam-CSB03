number = int(input('Input a positive number: '))
fib = [0]*(number + 1)
fib[1] = 1
print(fib)
for i in range(2,number+1):
    print(i, end='')
    fib[i] = fib[i - 1] + fib[i - 2]
print("First",number,"Fibonacci number(s):",*fib[1:])