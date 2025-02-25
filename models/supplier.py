from models.base_model import BaseModel

class Supplier(BaseModel):
    def add_supplier(self, name, contact, address):
        """ Adds a new supplier """
        query = """
        INSERT INTO suppliers (name, contact, address)
        VALUES (?, ?, ?)
        """
        self.execute_query(query, (name, contact, address))

    def update_supplier(self, supplier_id, name, contact, address):
        """ Updates an existing supplier """
        query = """
        UPDATE suppliers
        SET name = ?, contact = ?, address = ?
        WHERE id = ?
        """
        self.execute_query(query, (name, contact, address, supplier_id))

    def get_suppliers(self):
        return self.fetch_all("SELECT * FROM suppliers")

    def get_supplier(self, supplier_id):
        return self.fetch_one("SELECT * FROM suppliers WHERE id = ?", (supplier_id,))

    def delete_supplier(self, supplier_id):
        self.execute_query("DELETE FROM suppliers WHERE id = ?", (supplier_id,))
