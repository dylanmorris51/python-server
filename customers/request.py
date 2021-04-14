import sqlite3
import json
from models import Customer

CUSTOMERS = [
    {
        "id": 1,
        "name": "Hannah Hall",
        "address": "7002 Chestnut Ct",
        "email": "hannah@meanmrmustard.com"
    },
    {
        "id": 2,
        "name": "Bridgett Baker",
        "address": "7003 Chestnut Ct",
        "email": "Bridgett@bangingbakeries.com"
    },
    {
        "id": 3,
        "name": "Robert Towns",
        "address": "7004 Chestnut Ct",
        "email": "robert@derpderpderp.com"
    }
]

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


def create_customer(customer):
    max_id = CUSTOMERS[-1]["id"]
    new_id = max_id + 1
    customer["id"] = new_id
    CUSTOMERS.append(customer)
    return customer

def delete_customer(id):
    customer_index = -1

    for index, customer in enumerate(CUSTOMERS):
        if customer["id"] == id:
            customer_index = index

    if customer_index >= 0:
        CUSTOMERS.pop(customer_index)


def update_customer(id, new_customer):
    for index, customer in enumerate(CUSTOMERS):
        if customer["id"] == id:
            CUSTOMERS[index] = new_customer
            break