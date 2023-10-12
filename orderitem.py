import Order
import Product
class Orderitem(Order.Order, Product.Product):
    def __init__(self, first_name, last_name, address, cell_phone, email, gender, total_price, status, id, name, description, date_fabrication, is_active, quantity, unitary_price):
        super(Order, self).__init__(first_name, last_name, address, cell_phone, email, gender, total_price, status)
        super(Product, self).__init__(id, name, description, date_fabrication, is_active)
        self.quantity = quantity
        self.unitary_price = unitary_price