from helpers import(
   exit_program, 
   list_users,
   find_users_by_name,
   create_users,
   update_users,
   delete_users,
   find_products_by_name,
   create_products,
   list_products
)
def main():
    while True:
        menu()
        choice = input("> ")
        if choice == "0":
            exit_program()
        elif choice == "1":
            list_users()
        elif choice == "2":
            find_users_by_name()
        elif choice == "3":
            create_users()
        elif choice == "4":
            update_users()
        elif choice == "5":
            delete_users()
        elif choice == "6":
            find_products_by_name()
        elif choice == "7":
            create_products()
        elif choice == "8":
            list_products()
        else:
            print("Invalid choice")


def menu():
    print("Please select an option:")
    print("0. Exit")
    print("1. List all Users")
    print("2. Find Users by name")
    print("3. Create Users")
    print("4. Update Users")
    print("5. Delete Users")
    print("6. Find Products by name")
    print("7. Create Products")
    print("8. List all Products")


if __name__ == "__main__":
    main()
