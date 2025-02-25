from PyQt6.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget, QPushButton, QMenu
from views.customer_view import CustomerView
from views.product_view import ProductView
from views.supplier_view import SupplierView
from views.invoice_view import InvoiceView
from views.list_view import ListView
from controllers.customer_controller import CustomerController
from controllers.product_controller import ProductController
from controllers.supplier_controller import SupplierController
from controllers.invoice_controller import InvoiceController
from styles import MAIN_WINDOW_STYLE

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Business Management System")
        self.showMaximized()  # ✅ Fullscreen by default
        self.setStyleSheet(MAIN_WINDOW_STYLE)  # ✅ Apply global stylesheet

        # Initialize controllers
        self.customer_controller = CustomerController()
        self.product_controller = ProductController()
        self.supplier_controller = SupplierController()
        self.invoice_controller = InvoiceController()

        self.main_widget = QWidget()
        self.layout = QVBoxLayout(self.main_widget)

        self.menu_bar = self.menuBar()
        self.create_menu("Invoice", ["New Invoice", "View Invoice", "View Deleted"], self.invoice_action)
        self.create_menu("Customer", ["New Customer", "View Customers"], self.customer_action)
        self.create_menu("Supplier", ["New Supplier", "View Suppliers"], self.supplier_action)
        self.create_menu("Products", ["New Product", "View Products"], self.product_action)

        self.setCentralWidget(self.main_widget)

    def create_menu(self, title, actions, callback):
        """ Dynamically creates menus and connects actions to functions """
        menu = self.menu_bar.addMenu(title)
        for action_name in actions:
            action = menu.addAction(action_name)
            action.triggered.connect(lambda checked=False, name=action_name: callback(name))  # ✅ Fixed best practice

    ## ---------------------- ✅ Customer Actions ---------------------- ##
    def customer_action(self, action):
        """ Handles customer actions """
        print(f"Customer action triggered: {action}")  # ✅ Debugging print

        if action == "New Customer":
            print("Opening New Customer Window...")  # ✅ Debugging print
            self.customer_window = CustomerView(self.customer_controller)
            self.customer_window.show()
        elif action == "View Customers":
            self.list_window = ListView(
                "Customers",
                self.customer_controller.get_customers(),
                edit_callback=self.edit_customer,
                report_callback=self.customer_report,
                delete_callback=self.delete_customer
            )
            self.list_window.show()

    def delete_customer(self, customer):
        """ Deletes the selected customer from the database """
        customer_id = customer[0]
        self.customer_controller.delete_customer(customer_id)
        print(f"Deleted customer: {customer}")

    def edit_customer(self, customer):
        """ Opens customer edit form """
        if customer:
            self.edit_window = CustomerView(self.customer_controller)
            self.edit_window.name_input.setText(customer[1])
            self.edit_window.phone_input.setText(customer[2])
            self.edit_window.email_input.setText(customer[3])
            self.edit_window.address_input.setText(customer[4])
            self.edit_window.show()

    def customer_report(self, customer):
        print(f"Generating Report for Customer: {customer}")

    ## ---------------------- ✅ Supplier Actions ---------------------- ##
    def supplier_action(self, action):
        """ Handles supplier actions """
        print(f"Supplier action triggered: {action}")  # ✅ Debugging print

        if action == "New Supplier":
            print("Opening New Supplier Window...")  # ✅ Debugging print
            self.supplier_window = SupplierView(self.supplier_controller)
            self.supplier_window.show()
        elif action == "View Suppliers":
            self.list_window = ListView(
                "Suppliers",
                self.supplier_controller.get_suppliers(),
                edit_callback=self.edit_supplier,
                report_callback=self.supplier_report,
                delete_callback=self.delete_supplier
            )
            self.list_window.show()

    def delete_supplier(self, supplier):
        supplier_id = supplier[0]
        self.supplier_controller.delete_supplier(supplier_id)
        print(f"Deleted supplier: {supplier}")

    def edit_supplier(self, supplier):
        if supplier:
            self.edit_window = SupplierView(self.supplier_controller)
            self.edit_window.name_input.setText(supplier[1])
            self.edit_window.phone_input.setText(supplier[2])
            self.edit_window.address_input.setText(supplier[3])
            self.edit_window.show()

    def supplier_report(self, supplier):
        print(f"Generating Report for Supplier: {supplier}")

    ## ---------------------- ✅ Product Actions ---------------------- ##
    def product_action(self, action):
        """ Handles product actions """
        print(f"Product action triggered: {action}")  # ✅ Debugging print

        if action == "New Product":
            print("Opening New Product Window...")  # ✅ Debugging print
            self.product_window = ProductView(self.product_controller)
            self.product_window.show()
        elif action == "View Products":
            self.list_window = ListView(
                "Products",
                self.product_controller.get_products(),
                edit_callback=self.edit_product,
                report_callback=self.product_report,
                delete_callback=self.delete_product
            )
            self.list_window.show()

    def delete_product(self, product):
        product_id = product[0]
        self.product_controller.delete_product(product_id)
        print(f"Deleted product: {product}")

    def edit_product(self, product):
        if product:
            self.edit_window = ProductView(self.product_controller)
            self.edit_window.name_input.setText(product[1])
            self.edit_window.price_input.setText(str(product[2]))
            self.edit_window.show()

    def product_report(self, product):
        print(f"Generating Report for Product: {product}")

    ## ---------------------- ✅ Invoice Actions ---------------------- ##
    def invoice_action(self, action):
        """ Handles invoice actions """
        print(f"Invoice action triggered: {action}")  # ✅ Debugging print

        if action == "New Invoice":
            self.invoice_window = InvoiceView()
            self.invoice_window.show()
        elif action == "View Invoice":
            self.list_window = ListView(
                "Invoices",
                self.invoice_controller.get_invoices(),
                edit_callback=self.edit_invoice,
                report_callback=self.view_invoice_report,
                delete_callback=self.delete_invoice
            )
            self.list_window.show()
        elif action == "View Deleted":
            self.list_window = ListView(
                "Deleted Invoices",
                self.invoice_controller.get_deleted_invoices(),
                edit_callback=None,  # Cannot edit deleted invoices
                report_callback=self.view_deleted_invoice,
                delete_callback=None  # Cannot delete again
            )
            self.list_window.show()

    def edit_invoice(self, invoice):
        """ Open invoice in edit mode """
        invoice_id = invoice[0]
        self.invoice_window = InvoiceView(invoice_id=invoice_id)
        self.invoice_window.show()

    def delete_invoice(self, invoice):
        """ Moves invoice to the deleted section """
        invoice_id = invoice[0]
        self.invoice_controller.delete_invoice(invoice_id)
        print(f"Invoice {invoice_id} marked as deleted.")

    def view_deleted_invoice(self, invoice):
        """ View deleted invoice details """
        invoice_id = invoice[0]
        invoice_details = self.invoice_controller.get_invoice(invoice_id)
        invoice_items = self.invoice_controller.get_invoice_items(invoice_id)

        print(f"Viewing deleted invoice: {invoice_details}")
        for item in invoice_items:
            print(f"Item: {item}")

    def view_invoice_report(self, invoice):
        """ View invoice details """
        invoice_id = invoice[0]
        invoice_details = self.invoice_controller.get_invoice(invoice_id)
        invoice_items = self.invoice_controller.get_invoice_items(invoice_id)

        print(f"Viewing invoice: {invoice_details}")
        for item in invoice_items:
            print(f"Item: {item}")

if __name__ == "__main__":
    app = QApplication([])
    window = MainWindow()
    window.show()
    app.exec()
