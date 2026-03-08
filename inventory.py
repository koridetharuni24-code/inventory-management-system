inventory = []

def add_item():
    id = int(input("Enter Item ID: "))
    name = input("Enter Item Name: ")
    quantity = int(input("Enter Quantity: "))
    price = float(input("Enter Price: "))

    item = {
        "id": id,
        "name": name,
        "quantity": quantity,
        "price": price
    }

    inventory.append(item)
    print("Item added successfully!")

def display_items():
    if not inventory:
        print("Inventory is empty")
        return

    print("\nID\tName\tQuantity\tPrice")
    for item in inventory:
        print(item["id"], "\t", item["name"], "\t", item["quantity"], "\t\t", item["price"])

def search_item():
    id = int(input("Enter Item ID to search: "))

    for item in inventory:
        if item["id"] == id:
            print("Item Found")
            print("Name:", item["name"])
            print("Quantity:", item["quantity"])
            print("Price:", item["price"])
            return

    print("Item not found")

def update_item():
    id = int(input("Enter Item ID to update: "))

    for item in inventory:
        if item["id"] == id:
            item["quantity"] = int(input("Enter new quantity: "))
            print("Item updated successfully")
            return

    print("Item not found")

def delete_item():
    id = int(input("Enter Item ID to delete: "))

    for item in inventory:
        if item["id"] == id:
            inventory.remove(item)
            print("Item deleted successfully")
            return

    print("Item not found")

while True:
    print("\n--- Inventory Management System ---")
    print("1. Add Item")
    print("2. Display Items")
    print("3. Search Item")
    print("4. Update Item")
    print("5. Delete Item")
    print("6. Exit")

    choice = int(input("Enter choice: "))

    if choice == 1:
        add_item()

    elif choice == 2:
        display_items()

    elif choice == 3:
        search_item()

    elif choice == 4:
        update_item()

    elif choice == 5:
        delete_item()

    elif choice == 6:
        print("Exiting program")
        break

    else:
        print("Invalid choice")