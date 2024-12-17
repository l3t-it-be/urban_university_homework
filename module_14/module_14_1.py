import sqlite3


def create_table(cursor):
    cursor.execute(
        """CREATE TABLE IF NOT EXISTS Users
            (id INTEGER PRIMARY KEY,
            username TEXT NOT NULL UNIQUE,
            email TEXT NOT NULL UNIQUE,
            age INTEGER,
            balance INTEGER NOT NULL);
        """
    )


def insert_users(cursor, users_data):
    cursor.executemany(
        """INSERT OR IGNORE INTO Users
                (username, email, age, balance)
            VALUES
                (?, ?, ?, ?);
            """,
        users_data,
    )


def update_balances(cursor):
    cursor.execute(
        """UPDATE Users
           SET balance = ?
           WHERE id % 2 = 1;
            """,
        (500,),
    )


def delete_every_third_user(cursor):
    cursor.execute(
        """DELETE FROM Users
           WHERE id % 3 = 1;
        """
    )


def fetch_users(cursor):
    cursor.execute(
        """SELECT username, email, age, balance
            FROM Users
            WHERE age != 60;
        """
    )
    return cursor.fetchall()


def main():
    users_data = [
        (f'User{i}', f'example{i}@gmail.com', i * 10, 1000)
        for i in range(1, 11)
    ]

    with sqlite3.connect('not_telegram.db') as connection:
        cursor = connection.cursor()

        create_table(cursor)
        insert_users(cursor, users_data)
        update_balances(cursor)
        connection.commit()

        delete_every_third_user(cursor)
        connection.commit()

        users = fetch_users(cursor)
        for user in users:
            print(
                f'Имя: {user[0]} | Почта: {user[1]} | Возраст: {user[2]} | Баланс: {user[3]}'
            )


if __name__ == '__main__':
    main()
