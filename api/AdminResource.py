
class AdminResource:
    def __init__(self):
        self.room = None
        self._customer_email = None

    def get_customer(self, customer_email):
        self._customer_email = customer_email
        return f"{self.first_name}, {self.last_name}"

    def add_room(self, room):
        self.room = room

    def get_all_rooms(self):
        return

    def get_all_customers(self):
        return

    def display_all_reservations(self):
        return
