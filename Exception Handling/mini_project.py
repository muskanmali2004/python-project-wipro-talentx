def display_items(items):
    print("\n Available Items:")
    for item, price in items.items():
        print(f"- {item.title()} : ₹{price}")

def purchase_item(items):
    total = 0
    try:
        num_items = int(input("\n🛒 How many items do you want to purchase? "))
        for i in range(num_items):
            item = input(f"Enter item {i+1} name: ").lower()
            if item not in items:
                raise ValueError(f"{item} is not available in store!")
            qty = int(input(f"Enter quantity for {item}: "))
            cost = items[item] * qty
            print(f"{qty} x {item.title()} added to cart. Subtotal: ₹{cost}")
            total += cost
    except ValueError as ve:
        print("Error:", ve)
    except Exception as e:
        print("⚠️ Unexpected error:", e)
    else:
        print(f"\n🧾 Total Bill: ₹{total}")
    finally:
        print("Thank you for shopping with us!\n")

# Inventory dictionary
store_items = {
    "pen": 10,
    "notebook": 40,
    "eraser": 5,
    "pencil": 7,
    "marker": 25
}

# Main Program
print(" Welcome to Muskan's Stationery Store")
display_items(store_items)
purchase_item(store_items)
