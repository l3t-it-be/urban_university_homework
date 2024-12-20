import sqlite3


def initiate_db():
    with sqlite3.connect('products.db') as connection:
        cursor = connection.cursor()
        cursor.execute(
            """CREATE TABLE IF NOT EXISTS Products 
                    (id INTEGER PRIMARY KEY,
                    title TEXT NOT NULL,
                    description TEXT,
                    price INTEGER NOT NULL);
                """
        )


def get_all_products():
    with sqlite3.connect('products.db') as connection:
        cursor = connection.cursor()
        cursor.execute("""SELECT * FROM Products;""")
        products = cursor.fetchall()
    return products


def add_product(title, description, price):
    with sqlite3.connect('products.db') as connection:
        cursor = connection.cursor()
        cursor.execute(
            """SELECT * FROM Products 
                    WHERE title = ?;
                """,
            (title,),
        )
        existing_product = cursor.fetchone()
        if not existing_product:
            cursor.execute(
                """INSERT INTO Products 
                            (title, description, price) 
                        VALUES (?, ?, ?);
                            """,
                (title, description, price),
            )
