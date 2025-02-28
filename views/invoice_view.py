from PyQt6.QtWidgets import (
    QDialog, QVBoxLayout, QHBoxLayout, QLabel, QPushButton,
    QComboBox, QSpinBox, QTableWidget, QTableWidgetItem, QLineEdit, QDoubleSpinBox
)
from controllers.customer_controller import CustomerController
from controllers.product_controller import ProductController
from controllers.invoice_controller import InvoiceController

class InvoiceView(QDialog):
    def __init__(self, invoice_id=None, parent=None):
        super().__init__(parent)
        self.setWindowTitle("New Invoice" if invoice_id is None else "Edit Invoice")
        self.setGeometry(300, 200, 800, 500)

        self.invoice_id = invoice_id
        self.invoice_controller = InvoiceController()
        self.customer_controller = CustomerController()
        self.product_controller = ProductController()

        self.layout = QVBoxLayout()

        # Customer Selection
        customer_layout = QHBoxLayout()
        customer_layout.addWidget(QLabel("Customer:"))
        self.customer_dropdown = QComboBox()
        self.load_customers()
        customer_layout.addWidget(self.customer_dropdown)
        self.layout.addLayout(customer_layout)

        # Product Selection
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

        # Invoice Table
        self.invoice_table = QTableWidget()
        self.invoice_table.setColumnCount(5)
        self.invoice_table.setHorizontalHeaderLabels(["Product", "Price", "Quantity", "Total", "Delete"])
        self.layout.addWidget(self.invoice_table)

        # Payment Details
        payment_layout = QHBoxLayout()
        payment_layout.addWidget(QLabel("Amount Paid:"))
        self.amount_paid_input = QDoubleSpinBox()
        self.amount_paid_input.setMaximum(999999)
        payment_layout.addWidget(self.amount_paid_input)

        payment_layout.addWidget(QLabel("Payment Mode:"))
        self.payment_mode_dropdown = QComboBox()
        self.payment_mode_dropdown.addItems(["Cash", "Bank"])
        payment_layout.addWidget(self.payment_mode_dropdown)

        payment_layout.addWidget(QLabel("Narration:"))
        self.narration_input = QLineEdit()
        payment_layout.addWidget(self.narration_input)

        self.layout.addLayout(payment_layout)

        # Discount
        discount_layout = QHBoxLayout()
        discount_layout.addWidget(QLabel("Discount:"))
        self.discount_input = QDoubleSpinBox()
        self.discount_input.setMaximum(99999)
        self.discount_input.valueChanged.connect(self.update_grand_total)
        discount_layout.addWidget(self.discount_input)
        self.layout.addLayout(discount_layout)

        # Total Layout
        total_layout = QHBoxLayout()
        total_layout.addWidget(QLabel("Grand Total:"))
        self.grand_total_label = QLabel("0.00")
        total_layout.addWidget(self.grand_total_label)
        self.layout.addLayout(total_layout)

        # Buttons
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

    def save_invoice(self):
        """ Saves invoice to the database """
        customer_id = self.customer_dropdown.currentData()
        amount_paid = self.amount_paid_input.value()
        discount = self.discount_input.value()
        payment_mode = self.payment_mode_dropdown.currentText()
        narration = self.narration_input.text()

        total_amount = sum(item["total"] for item in self.invoice_items)

        formatted_items = [(item["product_id"], item["quantity"], item["price"], item["total"]) for item in self.invoice_items]

        if self.invoice_id:
            self.invoice_controller.update_invoice(self.invoice_id, customer_id, formatted_items, total_amount, amount_paid, discount, payment_mode, narration)
        else:
            self.invoice_controller.add_invoice(customer_id, formatted_items, total_amount, amount_paid, discount, payment_mode, narration)

        self.close()

    def update_grand_total(self):
        total_amount = sum(item["total"] for item in self.invoice_items)
        discount = self.discount_input.value()
        self.grand_total_label.setText(f"{total_amount - discount:.2f}")

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
        product_data = self.product_dropdown.currentData()

        if not product_data or product_data[0] == -1:
            return  

        product_id, price = product_data
        quantity = self.quantity_input.value()
        total = price * quantity

        # ✅ Ensure items are stored as a list of dictionaries
        for item in self.invoice_items:
            if item["product_id"] == product_id:
                item["quantity"] += quantity
                item["total"] = item["quantity"] * item["price"]
                self.refresh_invoice_table()
                return

        self.invoice_items.append({
            "product_id": product_id,
            "name": product_name,
            "price": price,
            "quantity": quantity,
            "total": total
        })

        self.refresh_invoice_table()

    def refresh_invoice_table(self):
        self.invoice_table.setRowCount(len(self.invoice_items))
        grand_total = 0

        for row, item in enumerate(self.invoice_items):
            self.invoice_table.setItem(row, 0, QTableWidgetItem(item['name']))
            self.invoice_table.setItem(row, 1, QTableWidgetItem(str(item['price'])))
            self.invoice_table.setItem(row, 2, QTableWidgetItem(str(item['quantity'])))
            self.invoice_table.setItem(row, 3, QTableWidgetItem(str(item['total'])))
            grand_total += item['total']

            delete_button = QPushButton("Delete")
            delete_button.clicked.connect(lambda _, p_id=item["product_id"]: self.delete_product(p_id))
            self.invoice_table.setCellWidget(row, 4, delete_button)

        self.grand_total_label.setText(f"{grand_total:.2f}")

    def delete_product(self, product_id):
        self.invoice_items = [item for item in self.invoice_items if item["product_id"] != product_id]
        self.refresh_invoice_table()
