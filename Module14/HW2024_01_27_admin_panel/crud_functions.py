import sqlite3


def db_connection_decorator(func):
    def wrapper(*args, **kwargs):
        conn = sqlite3.connect('my_db.db')
        cursor = conn.cursor()

        result = func(cursor, *args, **kwargs)

        conn.commit()
        conn.close()
        return result
    return wrapper


@db_connection_decorator
def initiate_db(cursor):
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS Products (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT NOT NULL,
    description TEXT,
    price integer NOT NULL,
    image_path TEXT NOT NULL)
''')


@db_connection_decorator
def get_all_products(cursor):

    cursor.execute('''SELECT * FROM Products''')
    products = cursor.fetchall()
    return products


@db_connection_decorator
def get_product_by_title(cursor, title):
    cursor.execute('''SELECT * FROM Products WHERE title = ?''', (title,))
    return cursor.fetchone()


@db_connection_decorator
def add_product(cursor=None, *args):
    for product in args:
        cursor.execute(f'''INSERT INTO Products (title, description, price, image_path)
        values (?, ?, ?, ?)''', (product['title'], product['description'], product['price'], product['image_path']))


if __name__ == '__main__':
    print(get_product_by_title('product1'))
