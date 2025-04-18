from catalog import Catalog

class Store:
    def __init__(self,name):
        self.name = name
        self.catalog = Catalog()
        self.customers = [] # list to store customer object
        self.sellers = [] # list to store seller object
        
    def authenticate_user(self,email,password):
        #check if the user is a customer
        for customer in self.customers:
            if customer.email == email and customer.password == password:
                return customer
        
        # check if the user is a seller
        
        for seller in self.sellers:
            if seller.email == email and seller.password == password:
                return seller
        
        #if no match is found
        return None
    