from models.base_model import BaseModel

class Invoice(BaseModel):
    def add_invoice(self, customer_id, items, total_amount):
        """ Saves invoice & its items in DB """
        query = """
        INSERT INTO transactions (customer_id, amount, transaction_type, is_deleted)
        VALUES (?, ?, 'debit', 0)
        """
        self.execute_query(query, (customer_id, total_amount))
        invoice_id = self.cursor.lastrowid  # Get the inserted invoice ID

        for product_id, quantity, price, total in items:
            self.execute_query(
                "INSERT INTO journals (transaction_id, product_id, amount, debit, quantity) VALUES (?, ?, ?, ?, ?)",
                (invoice_id, product_id, total, total, quantity)
            )

        return invoice_id

    def get_invoices(self):
        """ Retrieves non-deleted invoices """
        return self.fetch_all("""
            SELECT t.id, c.name, t.amount, t.created_at
            FROM transactions t
            JOIN customers c ON t.customer_id = c.id
            WHERE t.is_deleted = 0
        """)

    def get_invoice(self, invoice_id):
        """ Retrieves a specific invoice """
        return self.fetch_one("""
            SELECT t.id, c.name, t.amount, t.created_at
            FROM transactions t
            JOIN customers c ON t.customer_id = c.id
            WHERE t.id = ?
        """, (invoice_id,))

    def get_invoice_items(self, invoice_id):
        """ Retrieves all items in an invoice """
        return self.fetch_all("""
            SELECT p.name, j.quantity, j.amount
            FROM journals j
            JOIN products p ON j.product_id = p.id
            WHERE j.transaction_id = ?
        """, (invoice_id,))

    def delete_invoice(self, invoice_id):
        """ Marks invoice as deleted instead of removing it """
        self.execute_query("UPDATE transactions SET is_deleted = 1 WHERE id = ?", (invoice_id,))

    def get_deleted_invoices(self):
        """ Retrieves only deleted invoices """
        return self.fetch_all("""
            SELECT t.id, c.name, t.amount, t.created_at
            FROM transactions t
            JOIN customers c ON t.customer_id = c.id
            WHERE t.is_deleted = 1
        """)