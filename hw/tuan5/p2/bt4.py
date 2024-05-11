n = int(input("Number of items: "))
menu = []
pr = []
for i in range(n):
    item = input(f"Item {i+1}: ")
    price = float(input(f"Price of item {i+1}: "))
    menu.append((item, price))
    pr.append(price)
print(item)
average_price = sum(pr)/n
print(f"Average price: {average_price}")

above_average_items = [a for a in menu if a[1] > average_price]
print("Item(s) above average price:", *above_average_items)