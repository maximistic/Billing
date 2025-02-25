from controllers.base_controller import BaseController
from models.invoice import Invoice

class InvoiceController(BaseController):
    def __init__(self):
        super().__init__(Invoice())

    def add_invoice(self, customer_id, items, total_amount):
        return self.model.add_invoice(customer_id, items, total_amount)

    def get_invoices(self):
        return self.model.get_invoices()

    def delete_invoice(self, invoice_id):
        """ Soft delete an invoice (move to deleted section) """
        self.model.delete_invoice(invoice_id)

    def get_deleted_invoices(self):
        return self.model.get_deleted_invoices()
