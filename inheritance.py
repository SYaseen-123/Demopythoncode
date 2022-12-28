class Product:
    def __init__(self,Name,price,deal_price,rating):
         self.Name=Name
         self.price=price
         self.deal_price=deal_price
         self.rating=rating
    def Display_Product_Details(self):
         print(self.Name)
         print(self.price)
         print(self.deal_price)
         print(self.rating)
    def get_deal_price(self):
        return self.deal_price

class Electronic(Product):
    def set_warranty(self,warranty):
        self.warranty=warranty

    def get_warranty(self):
        print(self.warranty)

class Groceries(Product):
    #def __init__(self,Name,price,deal_price,rating,Expiry_date,package_date):
       # super().__init__(Name,price,deal_price,rating)
        #self.Expiry_date=Expiry_date
        #elf.package_date=package_date
    pass

    #def get_Expiry_date(self):
       # print(self.Expiry_date)
class Order:
    def __init__(self,delievery_speed,delievery_Address):
        self.items_in_cart=[]
        self.delievery_speed=delievery_speed
        self.delievery_Address=delievery_Address
    def add_item(self,product,quantity):
        self.items_in_cart.append((product,quantity))
    def display_order_details(self):
        for product,quantity in self.items_in_cart:
            product.Display_Product_Details()
            print("Quantity:{}".format(quantity))
    def display_total_bill(self):
        total_bill=0
        for product,quantity in self.items_in_cart:
            price=product.get_deal_price()*quantity
            total_bill+=price
            print("Total bill:{}".format(total_bill))
milk=Groceries("milk",78,28,7.9)
Laptop=Electronic("laptop",4500,3500,4)
order=Order("Delievery","vijayawada")
order.add_item(milk,3)
order.add_item(Laptop,1)
print("=============")
order.display_order_details()
print("===============")
order.display_total_bill()





