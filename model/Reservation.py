from model.Customer import Customer


class Reservation:
    def __init__(self):
        self._customers = []
        self._rooms = {}

    def store_customer(self, customer: Customer):
        self._customers.append(customer)

    def make_reservation(self, room: IRoom, check_in_date: Date, check_out_date: Date, customer: Customer):
        if room.is_free:
            room.create_room(room, check_in_date, check_out_date)
            self._rooms[room.get_room_number()] = customer
        else:
            print("unable to reserve room")

    # def make_reservation(self, room: IRoom, check_in_date: Date, check_out_date: Date):
    #     my_dict = {}
