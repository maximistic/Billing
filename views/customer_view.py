from PyQt6.QtWidgets import QDialog, QVBoxLayout, QPushButton, QLineEdit, QLabel

from PyQt6.QtWidgets import QDialog, QVBoxLayout, QPushButton, QLineEdit, QLabel

class CustomerView(QDialog):
    def __init__(self, controller, customer=None):
        super().__init__()
        self.controller = controller
        self.customer_id = customer[0] if customer else None  # ✅ Detect edit mode
        self.setWindowTitle("Edit Customer" if self.customer_id else "Add Customer")
        self.setFixedSize(500, 400)

        layout = QVBoxLayout()
        self.name_input = QLineEdit(customer[1] if customer else "")
        self.phone_input = QLineEdit(customer[2] if customer else "")
        self.email_input = QLineEdit(customer[3] if customer else "")
        self.address_input = QLineEdit(customer[4] if customer else "")

        layout.addWidget(QLabel("Name"))
        layout.addWidget(self.name_input)
        layout.addWidget(QLabel("Phone"))
        layout.addWidget(self.phone_input)
        layout.addWidget(QLabel("Email"))
        layout.addWidget(self.email_input)
        layout.addWidget(QLabel("Address"))
        layout.addWidget(self.address_input)

        save_button = QPushButton("Save")
        save_button.clicked.connect(self.save_customer)
        layout.addWidget(save_button)

        self.setLayout(layout)

    def save_customer(self):
        """ Save or update customer """
        name = self.name_input.text()
        phone = self.phone_input.text()
        email = self.email_input.text()
        address = self.address_input.text()

        if not name:
            print("Name is required!")
            return

        if self.customer_id:
            self.controller.update_customer(self.customer_id, name, phone, email, address)  # ✅ Update existing customer
            print("Customer updated successfully!")
        else:
            self.controller.add_customer(name, phone, email, address)  # ✅ Insert new customer
            print("Customer saved successfully!")

        self.close()