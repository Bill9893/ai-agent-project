

items = [
    {"name": "Apple", "price": 1.50},
    {"name": "Bread", "price": 2.50},
    {"name": "Milk", "price": 3.20}
]

total = 0
for item in items:
    total += item["price"]

print("====================")
print("Receipt".center(20))
print("====================")
for i, item in enumerate(items, 1):
    print(f"{i}. {item['name']:<10} ${item['price']:>2.2f}")
print("====================")
print(f"{'Total':<12} ${total:>2.2f}")