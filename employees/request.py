EMPLOYEES = [
    {
        "id": 1,
        "name": "George Harrison",
        "locationId": 1
    },
    {
        "id": 2,
        "name": "Keith Richards",
        "locationId": 2
    },
    {
        "id": 3,
        "name": "Jeff Buckley",
        "locationId": 2
    },
    {
        "id": 4,
        "name": "Brian May",
        "locationId": 1
    },
    {
        "name": "Hank Williams",
        "locationId": 2,
        "id": 5
    },
    {
        "id": 6,
        "name": "Joe Walsh",
        "locationId": 3
    }
]


def get_all_employees():
    return EMPLOYEES

def get_single_employee(id):
    requested_employee = None

    for employee in EMPLOYEES:
        if employee["id"] == id:
            requested_employee = employee
            return requested_employee