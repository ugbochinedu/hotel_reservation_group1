from typing import Type

from model.IRoom import IRoom
from model.RoomType import RoomType


class RoomClass(IRoom):

    def __init__(self):
        self._room_number: int = 0
        self._room_price: float = 0.0
        self._room_type = RoomType
        self._is_free: bool = False

    def set_room_number(self, room_number: int):
        self._room_number = room_number

    def get_room_number(self):
        return self._room_number

    def set_room_price(self, room_price: float):
        self._room_price = room_price

    def get_room_price(self):
        return self._room_price

    def set_room_type(self, room_type):
        self._room_type = room_type

    def get_room_type(self) -> Type[RoomType]:
        return self._room_type

    def set_is_free(self, room_is_free: bool):
        self._is_free = room_is_free

    def get_is_free(self):
        return self._is_free

    def __str__(self):
        return f""" 
        ROOM NUMBER: {self._room_number},      
        ROOM PRICE: {self._room_price},      
        ROOM TYPE: {self._room_type},      
        IS ROOM FREE: {self._is_free}      
        """

    def __repr__(self):
        return f""" 
        ROOM NUMBER: {self._room_number},      
        ROOM PRICE: {self._room_price},      
        ROOM TYPE: {self._room_type},      
        IS ROOM FREE: {self._is_free}      
        """
