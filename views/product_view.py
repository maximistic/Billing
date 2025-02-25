from PyQt6.QtWidgets import QDialog, QVBoxLayout, QPushButton, QLineEdit, QLabel

class ProductView(QDialog):
    def __init__(self, controller):
        super().__init__()
        self.controller = controller
        self.setWindowTitle("Add Product")
        self.setFixedSize(500, 400)

        layout = QVBoxLayout()

        self.name_input = QLineEdit()
        self.price_input = QLineEdit()

        layout.addWidget(QLabel("Product Name"))
        layout.addWidget(self.name_input)
        layout.addWidget(QLabel("Default Price"))
        layout.addWidget(self.price_input)

        add_button = QPushButton("Add Product")
        add_button.clicked.connect(self.add_product)
        layout.addWidget(add_button)

        self.setLayout(layout)

    def add_product(self):
        name = self.name_input.text()
        price = float(self.price_input.text())
        self.controller.add_product(name, price)
        self.close()
