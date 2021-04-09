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
    return CUSTOMERS

def get_single_customer(id):
    requested_customer = None

    for customer in CUSTOMERS:
        if customer["id"] == id:
            requested_customer = customer

        return requested_customer

def create_customer(customer):
    max_id = CUSTOMERS[-1]["id"]
    new_id = max_id + 1
    customer["id"] = new_id
    CUSTOMERS.append(customer)
    return customer