import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QStackedWidget
from UI.main_window import MainWindow
from utils.styles import load_stylesheet

class BillingApp(QApplication):
    def __init__(self, argv):
        super().__init__(argv)
        self.stylesheet = load_stylesheet()
        self.setStyleSheet(self.stylesheet)
        
        self.main_window = MainWindow()
        self.main_window.show()

if __name__ == "__main__":
    app = BillingApp(sys.argv)
    sys.exit(app.exec())