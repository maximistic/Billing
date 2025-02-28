from PyQt6.QtWidgets import (QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, 
                            QTabWidget, QPushButton, QLabel, QLineEdit,
                            QComboBox, QTableWidget, QTableWidgetItem,
                            QDateEdit, QHeaderView, QDoubleSpinBox, QStackedWidget)
from PyQt6.QtCore import Qt, QDate

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Billing System")
        self.setMinimumSize(1024, 768)
        self._setup_ui()
        
    def _setup_ui(self):
        # Main Layout
        main_widget = QWidget()
        self.setCentralWidget(main_widget)
        main_layout = QHBoxLayout(main_widget)
        
        # Navigation Sidebar
        nav_widget = QWidget()
        nav_layout = QVBoxLayout(nav_widget)
        nav_layout.setContentsMargins(0, 0, 0, 0)
        
        self.invoice_btn = QPushButton("Invoice")
        self.records_btn = QPushButton("Records")
        self.ledger_btn = QPushButton("Ledger")
        
        nav_layout.addWidget(self.invoice_btn)
        nav_layout.addWidget(self.records_btn)
        nav_layout.addWidget(self.ledger_btn)
        nav_layout.addStretch()
        
        # Main Content Area
        self.stacked_widget = QStackedWidget()
        
        # Add Pages
        self.invoice_ui = InvoiceUI()
        self.stacked_widget.addWidget(self.invoice_ui)
        
        main_layout.addWidget(nav_widget, stretch=1)
        main_layout.addWidget(self.stacked_widget, stretch=5)
        
        # Connect Signals
        self.invoice_btn.clicked.connect(
            lambda: self.stacked_widget.setCurrentWidget(self.invoice_ui))

class InvoiceUI(QWidget):
    def __init__(self):
        super().__init__()
        self._setup_invoice_ui()
        
    def _setup_invoice_ui(self):
        layout = QVBoxLayout(self)
        
        # Header Section
        header_widget = QWidget()
        header_layout = QHBoxLayout(header_widget)
        header_layout.addWidget(QLabel("Invoice Number:"))
        self.invoice_number = QLabel("INV-2023-001")
        header_layout.addWidget(self.invoice_number)
        header_layout.addStretch()
        header_layout.addWidget(QLabel("Date:"))
        self.date_edit = QDateEdit(QDate.currentDate())
        header_layout.addWidget(self.date_edit)
        header_widget.setProperty("class", "invoice-header")
        layout.addWidget(header_widget)
        
        # Customer Section
        customer_widget = QWidget()
        customer_layout = QHBoxLayout(customer_widget)
        customer_layout.addWidget(QLabel("Customer:"))
        self.customer_combo = QComboBox()
        self.customer_combo.addItems(["Customer 1", "Customer 2"])  # Temp data
        customer_layout.addWidget(self.customer_combo, stretch=1)
        layout.addWidget(customer_widget)
        
        # Product Entry Section
        product_entry_widget = QWidget()
        product_layout = QHBoxLayout(product_entry_widget)
        
        self.product_combo = QComboBox()
        self.product_combo.addItems(["Product 1", "Product 2"])  # Temp data
        self.quantity_spin = QDoubleSpinBox()
        self.quantity_spin.setRange(1, 9999)
        self.add_btn = QPushButton("Add Product")
        
        product_layout.addWidget(self.product_combo, stretch=3)
        product_layout.addWidget(QLabel("Qty:"))
        product_layout.addWidget(self.quantity_spin, stretch=1)
        product_layout.addWidget(self.add_btn, stretch=2)
        layout.addWidget(product_entry_widget)
        
        # Products Table
        self.products_table = QTableWidget(0, 4)
        self.products_table.setHorizontalHeaderLabels(
            ["Product", "Price", "Quantity", "Total"])
        self.products_table.horizontalHeader().setSectionResizeMode(
            QHeaderView.ResizeMode.Stretch)
        layout.addWidget(self.products_table)
        
        # Totals Section
        totals_widget = QWidget()
        totals_layout = QVBoxLayout(totals_widget)
        totals_layout.setContentsMargins(0, 15, 0, 0)
        
        # Discount and Payment
        discount_payment_widget = QWidget()
        dp_layout = QHBoxLayout(discount_payment_widget)
        
        dp_layout.addWidget(QLabel("Discount:"))
        self.discount_spin = QDoubleSpinBox()
        self.discount_spin.setPrefix("₹ ")
        dp_layout.addWidget(self.discount_spin)
        
        dp_layout.addWidget(QLabel("Payment Mode:"))
        self.payment_combo = QComboBox()
        self.payment_combo.addItems(["Cash", "Bank"])
        dp_layout.addWidget(self.payment_combo)
        
        totals_layout.addWidget(discount_payment_widget)
        
        # Totals Display
        totals_display_widget = QWidget()
        td_layout = QHBoxLayout(totals_display_widget)
        
        td_layout.addWidget(QLabel("Grand Total:"))
        self.grand_total_label = QLabel("₹ 0.00")
        td_layout.addWidget(self.grand_total_label)
        
        td_layout.addWidget(QLabel("Amount Paid:"))
        self.paid_amount = QLineEdit("0.00")
        td_layout.addWidget(self.paid_amount)
        
        totals_layout.addWidget(totals_display_widget)
        totals_widget.setProperty("class", "total-section")
        layout.addWidget(totals_widget)
        
        # Save Button
        self.save_btn = QPushButton("Save Invoice")
        layout.addWidget(self.save_btn, alignment=Qt.AlignmentFlag.AlignRight)