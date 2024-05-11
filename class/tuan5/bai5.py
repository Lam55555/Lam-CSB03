numbers = []
while True:
    a = int
lenth = len(numbers)
print(lenth)

for i in range(0, lenth - 1):
    for j in range(i + 1, lenth):
        if (numbers[i] > numbers[j]):
            tmp = numbers[i]
            numbers[i] = numbers[j]
            numbers[j] = tmp
print(numbers)