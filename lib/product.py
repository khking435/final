from config.config import conn, cursor


class Product:

    def __init__(self, name, price, id=None):
        self.id = id
        self.name = name
        self.price = price

    def __str__(self):
        return f"Product(id={self.id}, name={self.name}, price={self.price})"

    @classmethod
    def create_table(cls):
        sql = """
            CREATE TABLE IF NOT EXISTS products (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                price REAL NOT NULL
            )
        """
        cursor.execute(sql)
        conn.commit()

    @classmethod
    def drop_table(cls):
        sql = """DROP TABLE IF EXISTS products"""
        cursor.execute(sql)
        conn.commit()

    def save(self):
        sql = """INSERT INTO products (name, price) VALUES (?, ?)"""
        cursor.execute(
            sql,
            (
                self.name,
                self.price,
            ),
        )
        conn.commit()
        self.id = cursor.lastrowid

    @classmethod
    def get_all(cls):
        sql = """SELECT * FROM products"""
        cursor.execute(sql)
        rows = cursor.fetchall()
        return [cls(*row) for row in rows]

    @property
    def get_all_products(self):
        return self.get_all()

    @classmethod
    def get_by_id(cls, id):
        sql = """SELECT * FROM products WHERE id = ?"""
        cursor.execute(sql, (id,))
        row = cursor.fetchone()
        if row:
            return cls(*row)
        return None

    @classmethod
    def get_by_name(cls, name):
        sql = """SELECT * FROM products WHERE name = ?"""
        cursor.execute(sql, (name,))
        row = cursor.fetchone()
        if row:
            return cls(*row)
        return None

    @classmethod
    def get_by_price(cls, price):
        sql = """SELECT * FROM products WHERE price = ?"""
        cursor.execute(sql, (price,))
        row = cursor.fetchone()
        if row:
            return cls(*row)
        return None

    @classmethod
    def delete(cls, id):
        sql = """DELETE FROM products WHERE id = ?"""
        cursor.execute(sql, (id,))
        conn.commit()

    @classmethod
    def update(cls, id, name, price):
        sql = """UPDATE products SET name = ?, price = ? WHERE id = ?"""
        cursor.execute(sql, (name, price, id))
        conn.commit()

