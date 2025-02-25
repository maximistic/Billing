from PyQt6.QtWidgets import (
    QDialog, QVBoxLayout, QHBoxLayout, QLabel, QPushButton, 
    QComboBox, QSpinBox, QTableWidget, QTableWidgetItem
)
from controllers.customer_controller import CustomerController
from controllers.product_controller import ProductController
from controllers.invoice_controller import InvoiceController

class InvoiceView(QDialog):
    def __init__(self, invoice_id=None):
        super().__init__()
        self.setWindowTitle("New Invoice" if invoice_id is None else "Edit Invoice")
        self.setGeometry(300, 200, 600, 400)

        self.invoice_id = invoice_id
        self.invoice_controller = InvoiceController()
        self.customer_controller = CustomerController()
        self.product_controller = ProductController()

        self.layout = QVBoxLayout()

        customer_layout = QHBoxLayout()
        customer_layout.addWidget(QLabel("Customer:"))
        self.customer_dropdown = QComboBox()
        self.load_customers()
        customer_layout.addWidget(self.customer_dropdown)
        self.layout.addLayout(customer_layout)

        product_layout = QHBoxLayout()
        product_layout.addWidget(QLabel("Product:"))
        self.product_dropdown = QComboBox()
        self.load_products()
        self.product_dropdown.currentIndexChanged.connect(self.update_product_price)
        product_layout.addWidget(self.product_dropdown)

        product_layout.addWidget(QLabel("Price:"))
        self.price_label = QLabel("0.00")
        product_layout.addWidget(self.price_label)

        product_layout.addWidget(QLabel("Quantity:"))
        self.quantity_input = QSpinBox()
        self.quantity_input.setValue(1)
        self.quantity_input.valueChanged.connect(self.update_total_price)
        product_layout.addWidget(self.quantity_input)

        product_layout.addWidget(QLabel("Total:"))
        self.item_total_label = QLabel("0.00")
        product_layout.addWidget(self.item_total_label)

        self.layout.addLayout(product_layout)

        self.add_product_button = QPushButton("Add Product")
        self.add_product_button.clicked.connect(self.add_product_to_invoice)
        self.layout.addWidget(self.add_product_button)

        self.invoice_table = QTableWidget()
        self.invoice_table.setColumnCount(5)
        self.invoice_table.setHorizontalHeaderLabels(["Product", "Price", "Quantity", "Total", "Delete"])
        self.layout.addWidget(self.invoice_table)

        total_layout = QHBoxLayout()
        total_layout.addWidget(QLabel("Grand Total:"))
        self.grand_total_label = QLabel("0.00")
        total_layout.addWidget(self.grand_total_label)
        self.layout.addLayout(total_layout)

        button_layout = QHBoxLayout()
        self.save_button = QPushButton("Save Invoice")
        self.save_button.clicked.connect(self.save_invoice)
        button_layout.addWidget(self.save_button)

        self.cancel_button = QPushButton("Cancel")
        self.cancel_button.clicked.connect(self.close)
        button_layout.addWidget(self.cancel_button)

        self.layout.addLayout(button_layout)
        self.setLayout(self.layout)
        self.invoice_items = []

    def load_customers(self):
        customers = self.customer_controller.get_customers()
        self.customer_dropdown.addItem("Select Customer", -1)
        for customer in customers:
            self.customer_dropdown.addItem(customer[1], customer[0])

    def load_products(self):
        products = self.product_controller.get_products()
        self.product_dropdown.addItem("Select Product", -1)
        for product in products:
            self.product_dropdown.addItem(product[1], (product[0], product[2]))

    def update_product_price(self):
        _, price = self.product_dropdown.currentData() or (None, 0)
        self.price_label.setText(f"{price:.2f}")
        self.update_total_price()

    def update_total_price(self):
        _, price = self.product_dropdown.currentData() or (None, 0)
        quantity = self.quantity_input.value()
        total = price * quantity
        self.item_total_label.setText(f"{total:.2f}")

    def add_product_to_invoice(self):
        product_name = self.product_dropdown.currentText()
        product_id, price = self.product_dropdown.currentData() or (None, 0)
        quantity = self.quantity_input.value()
        total = price * quantity

        if product_id == -1:
            return

        self.invoice_items.append((product_id, quantity, price, total))
        self.refresh_invoice_table()

    def refresh_invoice_table(self):
        self.invoice_table.setRowCount(len(self.invoice_items))
        grand_total = 0

        for row, item in enumerate(self.invoice_items):
            for col, value in enumerate(item):
                self.invoice_table.setItem(row, col, QTableWidgetItem(str(value)))
            grand_total += item[3]

            delete_button = QPushButton("Delete")
            delete_button.clicked.connect(lambda _, r=row: self.delete_product(r))
            self.invoice_table.setCellWidget(row, 4, delete_button)

        self.grand_total_label.setText(f"{grand_total:.2f}")

    def delete_product(self, row):
        del self.invoice_items[row]
        self.refresh_invoice_table()

    def save_invoice(self):
        """ Saves invoice to the database """
        customer_id = self.customer_dropdown.currentData()
        if customer_id == -1:
            print("No customer selected")
            return

        total_amount = float(self.grand_total_label.text())
        if not self.invoice_items:
            print("No items in invoice")
            return

        if self.invoice_id:
            self.invoice_controller.update_invoice(self.invoice_id, customer_id, self.invoice_items, total_amount)
        else:
            self.invoice_controller.add_invoice(customer_id, self.invoice_items, total_amount)

        print("Invoice saved successfully")
        self.close()

