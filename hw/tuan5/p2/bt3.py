n = int(input("Input a positive number: "))
fib = [0]*(n + 1)
fib[1] = 1
for i in range(2, n + 1):
    fib[i] = fib[i - 1] + fib[i - 2]
print("First",n,"Fibonacci number(s):", *fib[1:])