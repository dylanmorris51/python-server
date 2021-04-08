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