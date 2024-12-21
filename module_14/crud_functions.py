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
        cursor.execute(
            """CREATE TABLE IF NOT EXISTS Users
                    (id INTEGER PRIMARY KEY,
                    username TEXT NOT NULL,
                    email TEXT NOT NULL,
                    age INTEGER NOT NULL,
                    balance INTEGER NOT NULL);
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


def add_user(username, email, age):
    with sqlite3.connect('products.db') as connection:
        cursor = connection.cursor()
        cursor.execute(
            """INSERT INTO Users
                        (username, email, age, balance)
                    VALUES (?, ?, ?, ?);
                        """,
            (username, email, age, 1000),
        )


def is_included(username):
    with sqlite3.connect('products.db') as connection:
        cursor = connection.cursor()
        cursor.execute(
            """SELECT * FROM Users
                    WHERE username = ?;
                """,
            (username,),
        )
        user = cursor.fetchone()
    return user is not None
