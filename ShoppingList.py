def add_to_list(shopping_list):
    while True:
        item = input("Enter an item to add to the shopping list (or 'done' to finish): ")
        if item.lower() == 'done':
            break
        shopping_list.append(item)

def remove_from_list(shopping_list):
    if not shopping_list:
        print("The shopping list is empty.")
        return

    print("Current items in the shopping list:")
    for index, item in enumerate(shopping_list, start=1):
        print(f"{index}. {item}")

    try:
        index_to_remove = int(input("Enter the number of the item to remove: "))
        if 1 <= index_to_remove <= len(shopping_list):
            del shopping_list[index_to_remove - 1]
            print("Item removed successfully.")
        else:
            print("Invalid input. Please enter a valid number.")
    except ValueError:
        print("Invalid input. Please enter a valid number.")

def print_shopping_list(shopping_list):
    if not shopping_list:
        print("The shopping list is empty.")
    else:
        print("Shopping List:")
        for item in shopping_list:
            print(f"- {item}")

def main():
    shopping_list = []
    while True:
        print("\nMenu:")
        print("1. Add item to shopping list")
        print("2. Remove item from shopping list")
        print("3. Print shopping list")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            add_to_list(shopping_list)
        elif choice == '2':
            remove_from_list(shopping_list)
        elif choice == '3':
            print_shopping_list(shopping_list)
        elif choice == '4':
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please enter a number from 1 to 4.")

if __name__ == "__main__":
    main()


