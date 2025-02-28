# Use PyQt6's QPrinter and QTextDocument
from PyQt6.QtPrintSupport import QPrinter
from PyQt6.QtGui import QTextDocument

class ReceiptGenerator:
    def __init__(self, invoice_data):
        self.invoice = invoice_data
        
    def print_receipts(self):
        self._print_receipt(template_type='customer')
        self._print_receipt(template_type='counter')
        
    def _print_receipt(self, template_type):
        printer = QPrinter(QPrinter.PrinterMode.HighResolution)
        doc = QTextDocument()
        html = self._generate_html(template_type)
        doc.setHtml(html)        
        doc.print(printer)