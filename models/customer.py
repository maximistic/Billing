from models.base_model import BaseModel

class Customer(BaseModel):
    def add_customer(self, name, phone, email, address):
        """ Adds a new customer to the database """
        query = """
        INSERT INTO customers (name, phone, email, address)
        VALUES (?, ?, ?, ?)
        """
        self.execute_query(query, (name, phone, email, address))

    def update_customer(self, customer_id, name, phone, email, address):
        """ Updates an existing customer """
        query = """
        UPDATE customers
        SET name = ?, phone = ?, email = ?, address = ?
        WHERE id = ?
        """
        self.execute_query(query, (name, phone, email, address, customer_id))

    def get_customers(self):
        return self.fetch_all("SELECT * FROM customers")

    def get_customer(self, customer_id):
        return self.fetch_one("SELECT * FROM customers WHERE id = ?", (customer_id,))

    def delete_customer(self, customer_id):
        self.execute_query("DELETE FROM customers WHERE id = ?", (customer_id,))