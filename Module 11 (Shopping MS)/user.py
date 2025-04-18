# Customer
# seller 
from abc import ABC
from order import Order
class User(ABC):
    def __init__(self,name,email,password):
        self.name = name
        self.email = email
        self.password = password
        
    
class Seller(User):
    def __init__(self, name, email, password):
        super().__init__(name, email, password)

    def add_product(self,store,product):
        store.catalog.add_product(product)
        
    def view_catalog(self,store):
        store.catalog.view_catalog()
    
class Customer(User):
    def __init__(self, name, email, password):
        super().__init__(name, email, password)
        self.cart = Order()
    
    def view_catalog(self,store):
        store.catalog.view_catalog()
        
    def add_to_cart(self,store,product_name,quantity):
        product = store.catalog.find_product(product_name)
        if product:
            if int(quantity) > int(product.quantity):
                print("Item Quantity Exceeded")
            else:
                product.quantity = quantity
                self.cart.add_product(product)
                print("Product Added to the Cart \n")
        else:
            print("Product Not Fount \n")
    
    def view_cart(self):
        self.cart.view_cart()
        
    def remove_from_cart(self,product):
        self.cart.remove(product)        
        
     