from PyQt6.QtWidgets import QDialog, QVBoxLayout, QPushButton, QLineEdit, QLabel

class CustomerView(QDialog):
    def __init__(self, controller):
        super().__init__()
        self.controller = controller
        self.setWindowTitle("Add Customer")

        layout = QVBoxLayout()

        self.name_input = QLineEdit()
        self.phone_input = QLineEdit()
        self.email_input = QLineEdit()
        self.address_input = QLineEdit()

        layout.addWidget(QLabel("Name"))
        layout.addWidget(self.name_input)
        layout.addWidget(QLabel("Phone"))
        layout.addWidget(self.phone_input)
        layout.addWidget(QLabel("Email"))
        layout.addWidget(self.email_input)
        layout.addWidget(QLabel("Address"))
        layout.addWidget(self.address_input)

        add_button = QPushButton("Add Customer")
        add_button.clicked.connect(self.add_customer)
        layout.addWidget(add_button)

        self.setLayout(layout)

    def add_customer(self):
        name = self.name_input.text()
        phone = self.phone_input.text()
        email = self.email_input.text()
        address = self.address_input.text()
        
        self.controller.add_customer(name, phone, email, address)
        self.close()
