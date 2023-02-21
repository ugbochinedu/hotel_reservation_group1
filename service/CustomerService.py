class CustomerService:
    def __init__(self):
        self.customers = {}

    def add_customer(self, email, first_name, last_name):
        self.customers[email] = {"first_name": first_name, "last_name": last_name}

    def get_customer(self, email):
        return self.customers.get(email)

    def get_all_customers(self):
        return list(self.customers.values())
