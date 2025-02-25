from PyQt6.QtWidgets import (
    QDialog, QVBoxLayout, QListWidget, QPushButton, QLineEdit, QHBoxLayout, QMessageBox
)

class ListView(QDialog):
    def __init__(self, title, items=None, edit_callback=None, report_callback=None, delete_callback=None):
        super().__init__()
        self.setWindowTitle(title)
        self.setGeometry(300, 200, 600, 400)
        self.items = items or []
        self.filtered_items = self.items
        self.edit_callback = edit_callback
        self.report_callback = report_callback
        self.delete_callback = delete_callback

        layout = QVBoxLayout()

        # Search Bar
        search_layout = QHBoxLayout()
        self.search_bar = QLineEdit()
        self.search_bar.setPlaceholderText("Search...")
        self.search_bar.textChanged.connect(self.filter_items)
        search_layout.addWidget(self.search_bar)
        layout.addLayout(search_layout)

        # List Widget
        self.list_widget = QListWidget()
        self.populate_list()
        self.list_widget.itemClicked.connect(self.enable_buttons)
        layout.addWidget(self.list_widget)

        # Buttons for Edit, Report, and Delete
        self.edit_button = QPushButton("Edit")
        self.edit_button.setEnabled(False)  # Initially disabled
        self.edit_button.clicked.connect(self.edit_selected_item)

        self.report_button = QPushButton("Report")
        self.report_button.setEnabled(False)  # Initially disabled
        self.report_button.clicked.connect(self.report_selected_item)

        self.delete_button = QPushButton("Delete")
        self.delete_button.setEnabled(False)  # Initially disabled
        self.delete_button.clicked.connect(self.delete_selected_item)

        button_layout = QHBoxLayout()
        button_layout.addWidget(self.edit_button)
        button_layout.addWidget(self.report_button)
        button_layout.addWidget(self.delete_button)
        layout.addLayout(button_layout)

        # Close Button
        close_button = QPushButton("Close")
        close_button.clicked.connect(self.close)
        layout.addWidget(close_button)

        self.setLayout(layout)

    def populate_list(self):
        """ Populates the list with filtered items, excluding ID & Timestamp """
        self.list_widget.clear()
        for item in self.filtered_items:
            if isinstance(item, tuple):  # Assuming data is like (id, name, phone, etc.)
                self.list_widget.addItem(item[1])  # Show only the name
            else:
                self.list_widget.addItem(str(item))  # Just in case

    def filter_items(self):
        """ Filters items based on search input """
        search_text = self.search_bar.text().strip().lower()
        self.filtered_items = [item for item in self.items if search_text in str(item[1]).lower()]
        self.populate_list()

    def enable_buttons(self):
        """ Enables Edit, Report, and Delete buttons when an item is selected """
        self.edit_button.setEnabled(True)
        self.report_button.setEnabled(True)
        self.delete_button.setEnabled(True)

    def get_selected_item(self):
        """ Returns selected item (full tuple) """
        selected = self.list_widget.currentItem()
        if selected:
            for item in self.items:
                if item[1] == selected.text():
                    return item  # Returns the full item tuple
        return None

    def edit_selected_item(self):
        """ Calls edit callback with selected item """
        selected_item = self.get_selected_item()
        if selected_item and self.edit_callback:
            self.edit_callback(selected_item)

    def report_selected_item(self):
        """ Calls report callback with selected item """
        selected_item = self.get_selected_item()
        if selected_item and self.report_callback:
            self.report_callback(selected_item)

    def delete_selected_item(self):
        """ Confirms and deletes selected item """
        selected_item = self.get_selected_item()
        if selected_item and self.delete_callback:
            confirmation = QMessageBox.question(
                self, "Confirm Deletion",
                f"Are you sure you want to delete {selected_item[1]}?",
                QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No
            )

            if confirmation == QMessageBox.StandardButton.Yes:
                self.delete_callback(selected_item)  # Call delete function
                self.items = [item for item in self.items if item != selected_item]  # Remove from list
                self.filter_items()  # Refresh list
