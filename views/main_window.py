from PyQt6.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget, QMenuBar, QPushButton, QMenu

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Business Management System")
        self.setGeometry(100, 100, 800, 600)

        self.main_widget = QWidget()
        self.layout = QVBoxLayout(self.main_widget)

        self.menu_bar = self.menuBar()
        self.create_menu("Invoice", ["New Invoice", "View Invoice", "Edit Invoice"], self.invoice_action)
        self.create_menu("Customer", ["New Customer", "View Customer", "Edit Customer"], self.customer_action)
        self.create_menu("Supplier", ["New Supplier", "View Supplier", "Edit Supplier"], self.supplier_action)
        self.create_menu("Products", ["New Product", "View Product", "Edit Product"], self.product_action)

        self.setCentralWidget(self.main_widget)

    def create_menu(self, title, actions, callback):
        menu = self.menu_bar.addMenu(title)
        for action_name in actions:
            action = menu.addAction(action_name)
            action.triggered.connect(lambda checked, name=action_name: callback(title, name))

    def invoice_action(self, category, action):
        print(f"{action} in {category}")

    def customer_action(self, category, action):
        print(f"{action} in {category}")

    def supplier_action(self, category, action):
        print(f"{action} in {category}")

    def product_action(self, category, action):
        print(f"{action} in {category}")

if __name__ == "__main__":
    app = QApplication([])
    window = MainWindow()
    window.show()
    app.exec()