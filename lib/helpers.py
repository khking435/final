from user import User
from product import Product

def exit_program():
    print("see you later!")
    exit()

def list_users():
    users = User.get_all_users()
    print_users(users)


def print_users(users):
    if users:
        for user in users:
            print(user)
    else:
        print("No users found.")


def find_users_by_name():
    name = input("Enter the user's name: ")
    user = User.find_by_name(name)
    print_user(user, name)


def print_user(user, name):
    if user:
        print(user)
    else:
        print(f'User {name} not found')


def create_users():
    try:
        name = input("Enter the user's name: ")
        password = input("Enter the user's password: ")
        user = User.create(name=name, password=password)
        print_user(user, name)
    except Exception as exc:
        print("Error creating user: ", exc)


def update_users():
    try:
        id_ = input("Enter the user's id: ")
        user = User.find_by_id(id_)
        if user:
            name = input("Enter the user's new name: ")
            user.name = name
            password = input("Enter the user's new password (optional): ")
            if password:
                user.password = password

            user.update()
            print_user(user, name)
        else:
            print(f'User {id_} not found')
    except Exception as exc:
        print("Error updating user: ", exc)


def delete_users():
    try:
        id_ = input("Enter the user's id: ")
        user = User.find_by_id(id_)
        if user:
            user.delete()
            print(f'User {id_} deleted')
        else:
            print(f'User {id_} not found')
    except Exception as exc:
        print("Error deleting user: ", exc)


def list_products():
    products = Product.get_all_products()
    print_products(products)


def print_products(products):
    if products:
        for product in products:
            print(product)
    else:
        print("No products found.")


def find_products_by_name():
    name = input("Enter the product's name: ")
    product = Product.find_by_name(name)
    print_product(product, name)


def print_product(product, name):
    if product:
        print(product)
    else:
        print(f'Product {name} not found')


def create_products():
    try:
        name = input("Enter the product's name: ")
        price = input("Enter the product's price: ")
        product = Product.create(name=name, price=price)
        print_product(product, name)
    except Exception as exc:
        print("Error creating product: ", exc)


        


