'''
Build a shopping cart system.
Use a dictionary for products and prices
Allow user to:
add items,remove items,view cart,
Calculate total bill using a function,Use a set to track unique items,Apply discount using conditions.
'''

products = {
    "apple": 50,
    "banana": 20,
    "milk": 60,
    "bread": 40
}

cart = {}             
unique_items = set()   


def calculate_total(cart):
    total = 0
    for item, qty in cart.items():
        total += products[item] * qty
    return total

while True:
    print("\n--- Shopping Cart Menu ---")
    print("1. Add item")
    print("2. Remove item")
    print("3. View cart")
    print("4. Checkout")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        item = input("Enter item name: ").lower()

        if item in products:
            qty = int(input("Enter quantity: "))
            cart[item] = cart.get(item, 0) + qty   
            unique_items.add(item)
            print("Item added to cart.")
        else:
            print("Item not available.")

    elif choice == "2":
        item = input("Enter item to remove: ").lower()

        if item in cart:
            del cart[item]
            unique_items.discard(item)
            print("Item removed from cart.")
        else:
            print("Item not in cart.")

    elif choice == "3":
        if not cart:
            print("Cart is empty.")
        else:
            print("\nItems in Cart:")
            for item, qty in cart.items():
                print(f"{item} x {qty} = ₹{products[item] * qty}")

            print("Unique items:", unique_items)

    elif choice == "4":
        total = calculate_total(cart)


        if total >= 500:
            discount = total * 0.10
            total -= discount
            print("10% discount applied!")

        print("Total Bill: ₹", total)
        print("Thank you for shopping!")
        break

    elif choice == "5":
        print("Exiting program...")
        break

    else:
        print("Invalid choice. Try again.")
