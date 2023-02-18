from abc import ABC, abstractmethod
from typing import Type

from model.RoomType import RoomType


class IRoom(ABC):

    @abstractmethod
    def set_room_number(self, room_number: int):
        pass

    @abstractmethod
    def get_room_number(self):
        pass

    @abstractmethod
    def set_room_price(self, room_price: float):
        pass

    @abstractmethod
    def get_room_price(self):
        pass

    @abstractmethod
    def set_room_type(self, room_type: float):
        pass

    @abstractmethod
    def get_room_type(self) -> Type[RoomType]:
        pass
    
    @abstractmethod
    def set_is_free(self, room_is_free: bool):
        pass

    @abstractmethod
    def get_is_free(self):
        pass
