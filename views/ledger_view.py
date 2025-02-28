from PyQt6.QtWidgets import QDialog, QVBoxLayout, QLabel, QPushButton, QComboBox, QLineEdit
from controllers.invoice_controller import InvoiceController

class LedgerView(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Ledger - Pay Balance")
        self.setGeometry(300, 200, 500, 300)

        self.invoice_controller = InvoiceController()

        self.layout = QVBoxLayout()
        
        self.customer_dropdown = QComboBox()
        self.load_customers()
        self.layout.addWidget(self.customer_dropdown)

        self.balance_label = QLabel("Balance: 0.00")
        self.layout.addWidget(self.balance_label)

        self.payment_amount = QLineEdit()
        self.payment_amount.setPlaceholderText("Enter Payment Amount")
        self.layout.addWidget(self.payment_amount)

        self.payment_method = QComboBox()
        self.payment_method.addItems(["Cash", "Bank"])
        self.layout.addWidget(self.payment_method)

        self.pay_button = QPushButton("Pay Now")
        self.pay_button.clicked.connect(self.pay_balance)
        self.layout.addWidget(self.pay_button)

        self.setLayout(self.layout)

    def load_customers(self):
        customers = self.invoice_controller.get_customers_with_balance()
        for customer in customers:
            self.customer_dropdown.addItem(f"{customer[1]} (Balance: {customer[2]})", customer[0])

    def pay_balance(self):
        customer_id = self.customer_dropdown.currentData()
        amount = float(self.payment_amount.text() or 0)
        payment_method = self.payment_method.currentText().lower()

        self.invoice_controller.update_payment(customer_id, amount)
        print(f"Paid {amount} via {payment_method} for Customer {customer_id}")

        self.close()
