from controllers.base_controller import BaseController
from models.supplier import Supplier

class SupplierController(BaseController):
    def __init__(self):
        super().__init__(Supplier())

    def add_supplier(self, name, phone, address):
        self.model.add_supplier(name, phone, address)

    def get_suppliers(self):
        return self.model.get_suppliers()

    def delete_supplier(self, supplier_id):
        self.model.delete_supplier(supplier_id)

    def update_supplier(self, supplier_id, name, phone, address):
        self.model.update_supplier(supplier_id, name, phone, address)