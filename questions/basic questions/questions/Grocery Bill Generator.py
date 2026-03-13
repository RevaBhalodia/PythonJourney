items = {}

while True:

    name = input("Enter item name (or 'done' to stop): ")

    if name == "done":
        break

    price = float(input("Enter price: "))

    items[name] = price

total = 0

print("\nBill Details")

for item, price in items.items():
    print(item, ":", price)
    total += price

print("Total Bill:", total)