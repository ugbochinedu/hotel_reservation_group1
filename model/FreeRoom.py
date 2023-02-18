class FreeRoom:
    def __init__(self):
        self._free_room_price: float = 0.0
        # self._is_free: bool = True

    def get_free_room_price(self):
        return self._free_room_price

    def __str__(self):
        return f""" 
        PRICE OF FREE ROOM: {self._free_room_price}     
        """

    def __repr__(self):
        return f""" 
        PRICE OF FREE ROOM: {self._free_room_price}     
        """
