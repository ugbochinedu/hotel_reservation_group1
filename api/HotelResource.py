
class HotelResource:

    def __init__(self):
        self._customer_reservation = ReservationService()
        self._customer = CustomerService()
        
        self._check_out_date = None
        self._check_in_date = None
        self._room_number = None
        self._email = None
        self._last_name = None
        self._first_name = None
        self._customer_mail = None

    def add_customer(self, first_name, last_name, email):
        self._first_name = first_name
        self._last_name = last_name
        self._email = email

    def create_customer(self, first_name, last_name, email):
        self._first_name = first_name
        self._last_name = last_name
        self._email = email

    def get_customer(self, customer_email):
        return self._customer_service.get_customer(customer_email)

    def get_all_customers(self):
        pass

    def book_a_room(self, customer_email, room, check_in_date, check_out_date):
        self._check_in_date = check_in_date
        self._customer_mail = customer_email
        self._room_number = room
        self._check_out_date = check_out_date

    def get_room(self, room_number):
        return self._reservation_service.get_room(room_number)

    def get_customer_reservations(self, customer_email):
        return self._customer_reservation.get_customer_reservations(customer_email)

    def find_a_room(self, check_in, check_out):
        self._check_in_date = check_in
        self._check_out_date = check_out
        return self._findroom
