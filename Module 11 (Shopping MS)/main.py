from catalog import Catalog
from order import Order
from store import Store
from user import Seller,Customer
from product import Product
daraz = Store('Daraz')

def customer_site(customer):
    while True:
        print(f"Welcome our store {customer.name}")
        print("1. View Catalog")
        print("2. Add product to the Cart")
        print('3. View Cart')
        print("4. Remove Product from the cart")
        print('5. Exit')
        
        try:
            choice = int(input("Enter your choice: "))
        except ValueError:
            print("Invalid input. Please enter a number.")
            continue
        
        if choice == 1:
            customer.view_catalog(daraz)
        elif choice == 2:
            product_name = input("Enter the product Name: ")
            quantity = int(input("Enter the quantity: "))
            customer.add_to_cart(daraz,product_name,quantity)
        elif choice == 3:
            customer.view_cart()
        elif choice == 4:
            product_name = input("Enter product name: ")
            customer.cart.remove(product_name)
        elif choice == 5:
            break
        else:
            print("Invalid Choice")
    
def Seller_site(seller):
    while True:
        print(f"Welcome our site {seller.name}")
        print("1. View Catalog")
        print("2. Add product to the Store")
        print('3. Exit')
        
        try:
            choice = int(input("Enter your choice: "))
        except ValueError:
            print("Invalid input. Please enter a number.")
            continue
        
        if choice == 1:
            seller.view_catalog(daraz)
        elif choice == 2:
            name = input("Enter the product Name: ")
            price = int(input("Enter product price: "))
            quantity = int(input("Enter the quantity: "))
            product = Product(name,price,quantity)
            seller.add_product(daraz,product)
        elif choice == 3:
            break
        else:
            print("Invalid Choice")

while True:
    print("----------Welcome-----------")
    print("1. Sing up as a Customer")
    print('2. Sign up as a Seller')
    print('3. login ')
    print('4. Exit')
    
    try:
        choice = int(input("Enter your choice: "))
    except ValueError:
        print("Invalid input. Please enter a number.")
        continue
    
    if choice == 1:
        name = input("Enter Your Name: ")
        email = input("Enter your Email: ")
        password = input("Enter your password: ")
        if any(customer.email == email for customer in daraz.customers):
            print("A customer with this email already exists. Please try logging in.")
            continue
        customer = Customer(name=name,email=email,password=password)
        daraz.customers.append(customer)
        customer_site(customer)
    elif choice == 2:
        name = input("Enter Your Name: ")
        email = input("Enter your Email: ")
        password = input("Enter your password: ")
        if any(seller.email == email for seller in daraz.sellers):
            print("A seller with this email already exists. Please try logging in.")
            continue
        seller = Seller(name=name,email=email,password=password)
        daraz.sellers.append(seller)
        Seller_site(seller)
    elif choice == 3:
        email = input("Enter your Email: ")
        password = input("Enter your password: ")
        
        user = daraz.authenticate_user(email, password)
        if user:
            if isinstance(user, Customer):
                print("Login successful as Customer!")
                customer_site(user)
            elif isinstance(user, Seller):
                print("Login successful as Seller!")
                Seller_site(user)
        else:
            print("Invalid email or password. Please try again.")
    else:
        break