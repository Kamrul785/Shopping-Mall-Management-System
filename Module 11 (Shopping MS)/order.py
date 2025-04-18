class Order:
    def __init__(self):
        self.list = {}
        
    def add_product(self,product):
        if product in self.list:
            self.list[product] += int(product.quantity)
        else:
            self.list[product] = int(product.quantity)
    
    def remove(self, product_name):
        for product in list(self.list.keys()):
            if product.name == product_name:
                del self.list[product]
                print(f"{product_name} removed from the cart.")
                return
        print(f"{product_name} not found in the cart.")
    
    def view_cart(self):
        print("------------View Cart-------------")
        print(f'{"product_name":<15}{"quantity":<11}{"price":<10}') 
        for product, quantity in self.list.items():
            print(f'{product.name:<15}{quantity:<11}{product.price:<10}')       
        print(f"Total Price: {self.total_price}")
        
    @property
    def total_price(self):
        return sum(product.price * quantity for product, quantity in self.list.items())
    
    def clear(self):
        self.list = {}