def load_stylesheet():
    return """
    /* Base Styling */
    QWidget {
        font-family: 'Segoe UI', Arial;
        font-size: 10pt;
        color: #2c3e50;
    }
    
    QHeaderView::section {
        background-color: #3498db;
        color: white;
        padding: 6px;
    }
    
    QPushButton {
        background-color: #3498db;
        color: white;
        border: none;
        padding: 8px 16px;
        border-radius: 4px;
    }
    
    QPushButton:hover {
        background-color: #2980b9;
    }
    
    /* Invoice Specific */
    .invoice-header {
        background-color: #ecf0f1;
        padding: 15px;
        border-radius: 5px;
        margin-bottom: 10px;
    }
    
    .total-section {
        background-color: #f9f9f9;
        border: 1px solid #ddd;
        padding: 15px;
        border-radius: 5px;
    }
    
    /* Table Styling */
    QTableView {
        border: 1px solid #ddd;
        alternate-background-color: #f8f9fa;
    }
    
    QTableCornerButton::section {
        background-color: #3498db;
    }
    """