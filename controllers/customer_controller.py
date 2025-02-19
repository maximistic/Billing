from controllers.base_controller import BaseController
from models.customer import Customer

class CustomerController(BaseController):
    def __init__(self):
        super().__init__(Customer())

    def add_customer(self, name, phone, email, address):
        self.model.add_customer(name, phone, email, address)

    def get_customers(self):
        return self.model.get_customers()

    def delete_customer(self, customer_id):
        self.model.delete_customer(customer_id)
