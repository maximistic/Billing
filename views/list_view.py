from PyQt6.QtWidgets import (
    QDialog, QVBoxLayout, QListWidget, QPushButton, QLineEdit, 
    QHBoxLayout, QMessageBox
)

class ListView(QDialog):
    def __init__(self, title, items=None, edit_callback=None, report_callback=None, delete_callback=None):
        super().__init__()
        self.setWindowTitle(title)
        self.setGeometry(300, 200, 600, 400)
        self.items = items or []  # List of tuples (invoice_id, name, price)
        self.filtered_items = self.items
        self.edit_callback = edit_callback
        self.report_callback = report_callback
        self.delete_callback = delete_callback

        layout = QVBoxLayout()

        # 🔍 Search Bar
        search_layout = QHBoxLayout()
        self.search_bar = QLineEdit()
        self.search_bar.setPlaceholderText("Search...")
        self.search_bar.textChanged.connect(self.filter_items)
        search_layout.addWidget(self.search_bar)
        layout.addLayout(search_layout)

        # 📋 List Widget
        self.list_widget = QListWidget()
        self.populate_list()
        self.list_widget.itemClicked.connect(self.enable_buttons)
        layout.addWidget(self.list_widget)

        # 🛠 Buttons (Edit, Report, Delete)
        self.edit_button = QPushButton("Edit")
        self.edit_button.setEnabled(False)
        self.edit_button.clicked.connect(self.edit_selected_item)

        self.report_button = QPushButton("Report")
        self.report_button.setEnabled(False)
        self.report_button.clicked.connect(self.report_selected_item)

        self.delete_button = QPushButton("Delete")
        self.delete_button.setEnabled(False)
        self.delete_button.clicked.connect(self.delete_selected_item)

        button_layout = QHBoxLayout()
        button_layout.addWidget(self.edit_button)
        button_layout.addWidget(self.report_button)
        button_layout.addWidget(self.delete_button)
        layout.addLayout(button_layout)

        # ❌ Close Button
        close_button = QPushButton("Close")
        close_button.clicked.connect(self.close)
        layout.addWidget(close_button)

        self.setLayout(layout)

    def populate_list(self):
        """ Populates the list with filtered items. Shows price only for invoices. """
        self.list_widget.clear()
        for item in self.filtered_items:
            if isinstance(item, tuple) and len(item) >= 3:
                if "Invoice" in self.windowTitle():
                    try:
                        price = float(item[2])  
                        invoice_text = f"{item[1]} - ₹{price:.2f}"  
                    except ValueError:
                        invoice_text = f"{item[1]} - ₹{item[2]}"  
                else:
                    invoice_text = item[1]  
            else:
                invoice_text = str(item)  

            self.list_widget.addItem(invoice_text)

    def filter_items(self):
        """ Filters invoices based on search input """
        search_text = self.search_bar.text().strip().lower()
        self.filtered_items = [
            item for item in self.items if search_text in str(item[1]).lower()
        ]
        self.populate_list()

    def enable_buttons(self):
        """ Enables buttons when an invoice is selected """
        self.edit_button.setEnabled(True)
        self.report_button.setEnabled(True)
        self.delete_button.setEnabled(True)

    def get_selected_item(self):
        """ Returns the full tuple of the selected invoice """
        selected = self.list_widget.currentItem()
        if selected:
            for item in self.items:
                invoice_text = f"{item[1]} - ₹{item[2]:.2f}"
                if invoice_text == selected.text():
                    return item 
        return None

    def edit_selected_item(self):
        """ Calls edit callback with selected invoice """
        selected_item = self.get_selected_item()
        if selected_item and self.edit_callback:
            self.edit_callback(selected_item)

    def report_selected_item(self):
        """ Calls report callback with selected invoice """
        selected_item = self.get_selected_item()
        if selected_item and self.report_callback:
            self.report_callback(selected_item)

    def delete_selected_item(self):
        """ Confirms and deletes selected invoice """
        selected_item = self.get_selected_item()
        if selected_item and self.delete_callback:
            confirmation = QMessageBox.question(
                self, "Confirm Deletion",
                f"Are you sure you want to delete {selected_item[1]}?",
                QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No
            )

            if confirmation == QMessageBox.StandardButton.Yes:
                self.delete_callback(selected_item)
                self.items = [item for item in self.items if item != selected_item]
                self.filter_items()
