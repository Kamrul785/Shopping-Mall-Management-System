class Catalog:
    def __init__(self):
        self.catalog = [] # catalog er database
    
    def add_product(self,product):
        self.catalog.append(product)
    
    def find_product(self,product_name):
        for product in self.catalog:
            if product.name.lower() ==  product_name.lower():
                return product
        return None
    
    def view_catalog(self):
        print("-------Catalog--------")
        print("Product Name\tPrice\tQuantity")
        for product in self.catalog:
            print(f'{product.name:<15}\t{product.price:<15}\t{product.quantity}')