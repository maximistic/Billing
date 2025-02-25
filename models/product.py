from models.base_model import BaseModel

class Product(BaseModel):
    def add_product(self, name, price):
        query = """
        INSERT INTO products (name, price) 
        VALUES (?, ?)
        """
        self.execute_query(query, (name, price))

    def get_products(self):
        return self.fetch_all("SELECT * FROM products")

    def get_product(self, product_id):
        return self.fetch_one("SELECT * FROM products WHERE id = ?", (product_id,))

    def delete_product(self, product_id):
        self.execute_query("DELETE FROM products WHERE id = ?", (product_id,))

    def update_product(self, product_id, name, price):
        query = """
        UPDATE products 
        SET name = ?, price = ? 
        WHERE id = ?
        """
        self.execute_query(query, (name, price, product_id))
