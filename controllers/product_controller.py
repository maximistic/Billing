from controllers.base_controller import BaseController
from models.product import Product

class ProductController(BaseController):
    def __init__(self):
        super().__init__(Product())

    def add_product(self, name, price):
        self.model.add_product(name, price)

    def get_products(self):
        return self.model.get_products()
