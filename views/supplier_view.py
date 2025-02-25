from PyQt6.QtWidgets import QDialog, QVBoxLayout, QPushButton, QLineEdit, QLabel

class SupplierView(QDialog):
    def __init__(self, controller):
        super().__init__()
        self.controller = controller
        self.setWindowTitle("Add Supplier")
        self.setFixedSize(500, 400)

        layout = QVBoxLayout()

        self.name_input = QLineEdit()
        self.phone_input = QLineEdit()
        self.address_input = QLineEdit()

        layout.addWidget(QLabel("Supplier Name"))
        layout.addWidget(self.name_input)
        layout.addWidget(QLabel("Phone"))
        layout.addWidget(self.phone_input)
        layout.addWidget(QLabel("Address"))
        layout.addWidget(self.address_input)

        add_button = QPushButton("Add Supplier")
        add_button.clicked.connect(self.add_supplier)
        layout.addWidget(add_button)

        self.setLayout(layout)

    def add_supplier(self):
        name = self.name_input.text()
        phone = self.phone_input.text()
        address = self.address_input.text()
        
        self.controller.add_supplier(name, phone, address)
        self.close()
