import Client
class Order(Client.Client):
   def __init__(self, first_name, last_name, address, cell_phone, email, gender, total_price, status):
    super().__init__(first_name, last_name, address, cell_phone, email, gender)
      self.total_price = total_price
      self.status = status