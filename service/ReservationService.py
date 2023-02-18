class ReservationService:

    def __init__(self):
        self._room_number = Room()
        self._room = IRoom()
        self._room_id: str = ""
        self._customer = Customer()
        self._check_in_date = Date()
        self._check_out_date = Date()

    def add_room(self, room):
        if self._room == room:
            return room

    def get_room(self, room_id):
        if self._room_id == room_id:
            return room_id

    def reserve_a_room(self, customer, room, check_in_date, check_out_date):
        if self._customer == customer and self._room == room and self._check_in_date == check_in_date \
                and self._check_out_date == check_out_date:
            return "Your room as been reserved"

    def find_rooms(self, check_in_date, check_out_date):
        if self._check_in_date == check_in_date and self._check_out_date == check_out_date:
            return "Room as been booked"

    def get_customers_reservations(self, customer):
        if self._customer == customer:
            return customer

    def print_reservation(self):
        return f"""
        Customer details {self._customer},
        Check_in-date {self._check_in_date},
        Check_out-date{self._check_out_date},
        Room Id {self._room_id},
        Room number {self._room_number}
        """

    def __repr__(self):
        return f"""
        Rooms {self._room},
        Customer details {self._customer},
        Check_in-date {self._check_in_date},
        Check_out-date{self._check_out_date},
        Room Id {self._room_id},
        Room number {self._room_number}
        """

    def __str__(self):
        return f"""
        Rooms {self._room},
        Customer details {self._customer},
        Check_in-date {self._check_in_date},
        Check_out-date{self._check_out_date},
        Room Id {self._room_id},
        Room number {self._room_number}
        """
