# styles.py

MAIN_WINDOW_STYLE = """
    QMainWindow {
        background-color: #2C3E50;  /* Dark Blue */
        color: white;
    }
    QMenuBar {
        background-color: #34495E;
        color: white;
    }
    QMenuBar::item {
        background-color: transparent;
        padding: 5px;
    }
    QMenuBar::item:selected {
        background-color: #1ABC9C;
    }
"""

FORM_STYLE = """
    QDialog {
        background-color: #ECF0F1; /* Light Gray */
        border: 2px solid #2980B9; /* Blue Border */
        border-radius: 10px;
    }
    QLabel {
        font-size: 14px;
        font-weight: bold;
    }
    QLineEdit, QSpinBox, QComboBox {
        background-color: white;
        border: 1px solid #2980B9;
        padding: 5px;
    }
    QPushButton {
        background-color: #3498DB;
        color: white;
        padding: 7px;
        border-radius: 5px;
    }
    QPushButton:hover {
        background-color: #2980B9;
    }
"""

LIST_VIEW_STYLE = """
    QDialog {
        background-color: #ECF0F1;
        border: 2px solid #27AE60; /* Green Border */
        border-radius: 10px;
    }
    QListWidget {
        background-color: white;
        border: 1px solid #27AE60;
        padding: 5px;
    }
    QLineEdit {
        border: 1px solid #27AE60;
        padding: 5px;
    }
    QPushButton {
        background-color: #2ECC71;
        color: white;
        padding: 7px;
        border-radius: 5px;
    }
    QPushButton:hover {
        background-color: #27AE60;
    }
"""
