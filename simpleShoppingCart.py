items = [
    {"name": "Apple", "price": 1.50},
    {"name": "Bread", "price": 2.50},
    {"name": "Milk", "price": 3.20},
    {"name": "Eggs", "price": 2.00},
    {"name": "Cheese", "price": 4.00}
]

def available_items(items):
    print("====================")
    print("Available Items".center(20))
    print("====================")
    for i, item in enumerate(items, 1):
        print(f"{i}. {item['name']:<10} ${item['price']:>2.2f}")
    print("====================")

available_items(items)



def print_receipt(cart):
    total = sum(item["price"] for item in cart)
    print("====================")
    print("Receipt".center(20))
    print("====================")
    for i, item in enumerate(cart, 1):
        print(f"{i}. {item['name']:<10} ${item['price']:>2.2f}")
    print("====================")
    print(f"{'Total':<12} ${total:>2.2f}")


cart = []

while True:
    choice = input("Enter the number of the item you want to add to your cart: ")
    if choice == "done":
        break
    try:
        choice = int(choice)
        if 1 <= choice <= len(items):
            cart.append(items[choice - 1])
            print(f"Added {items[choice - 1]['name']} to your cart.")
        else:
            print("Invalid choice. Please try again.")
    except ValueError:
        print("Invalid choice. Please try again.")



print_receipt(cart)