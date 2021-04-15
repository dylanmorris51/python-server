import sqlite3
import json
from models import Employee


def get_all_employees():
    with sqlite3.connect("./kennel.db") as conn:

        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        db_cursor.execute("""
            SELECT
                e.id,
                e.name,
                e.location_id
            FROM employee e
        """)

        employees = []
        dataset = db_cursor.fetchall()

        for row in dataset:
            employee = Employee(row['id'], row['name'], row['location_id'])

            employees.append(employee.__dict__)

        return json.dumps(employees)

def get_single_employee(id):
    with sqlite3.connect("./kennel.db") as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        db_cursor.execute("""
            SELECT
                e.id,
                e.name,
                e.location_id
            FROM employee e
            WHERE e.id = ?
        """, (id,))

        data = db_cursor.fetchone()

        employee = Employee(data['id'], data['name'], data['location_id'])
        return json.dumps(employee.__dict__)

def get_employees_by_location(location_id):

    with sqlite3.connect("./kennel.db") as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        db_cursor.execute("""
            SELECT
                e.id,
                e.name,
                e.location_id
            FROM employee e
            WHERE e.location_id = ?
        """, (location_id,))

        employees = []
        dataset = db_cursor.fetchall()

        for row in dataset:
            employee = Employee(row['id'], row['name'], row['location_id'])
            employees.append(employee.__dict__)

    return json.dumps(employees)