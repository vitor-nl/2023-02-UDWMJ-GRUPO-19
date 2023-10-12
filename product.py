import Category
class Product(Category.Category):
    def __init__(self, id, name, description, date_fabrication, is_active):
        super().__init__(id, name, description)
        self.date_fabrication = date_fabrication
        self.is_active = is_active