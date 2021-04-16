import sqlite3
import json
from models import Customer


def get_all_customers():
    with sqlite3.connect("./kennel.db") as conn:

        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        db_cursor.execute("""
            SELECT
                c.id,
                c.name,
                c.address,
                c.email
            FROM customer c
        """)

        customers = []
        dataset = db_cursor.fetchall()

        for row in dataset:
            customer = Customer(row['id'], row['name'], row['address'], row['email'])

            customers.append(customer.__dict__)        

        return json.dumps(customers)


def get_single_customer(id):
    with sqlite3.connect("./kennel.db") as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        db_cursor.execute("""
            SELECT
                c.id,
                c.name,
                c.address,
                c.email
            FROM customer c
            WHERE c.id = ?
        """, (id,))

        data = db_cursor.fetchone()

        customer = Customer(data['id'], data['name'], data['address'], data['email'])
        return json.dumps(customer.__dict__)


def get_customers_by_email(email):

    with sqlite3.connect("./kennel.db") as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        # Write the SQL query to get the info you want
        db_cursor.execute("""
            select
                c.id,
                c.name,
                c.address,
                c.email,
                c.password
            from customer c
            WHERE c.email = ?
        """, (email,))

        customers = []
        dataset = db_cursor.fetchall()

        for row in dataset:
            customer = Customer(row['id'], row['name'], row['address'], row['email'], row['password'])
            customers.append(customer.__dict__)

    return json.dumps(customers)