from model.Customer import Customer


class Reservation:
    customers = []

    def store_customer(self, customer: Customer):
        self.customers.append(customer)

    def reserve_room(self, room: IRoom, check_in_date: Date, check_out_date: Date, customer: Customer):
        if room.is_free:
            room.create_room(room, check_in_date, check_out_date)
        else:
            print("unable to reserve room")
