class HotelResource:

    def add_customer(self, first_name, last_name, email):
        self.customer.set_first_name(first_name)
        self.customer.set_last_name(last_name)
        self.customer.set_email(email)

    def create_customer(self, first_name, last_name, email):
        self.customer.set_first_name(first_name)
        self.customer.set_last_name(last_name)
        self.customer.set_email(email)

    def get_customer(self, customer_email):
        self.customer.get_customer(customer_email)

    def get_all_customers(self):
        pass

    def get_room(self, room_number):
        self.IR