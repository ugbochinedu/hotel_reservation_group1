import enum


class RoomType(enum.Enum):
    SINGLE = 25000
    DOUBLE = 50000
    EXECUTIVE = 75000

    def __str__(self):
        return f""" 
        SINGLE ROOM: {self.SINGLE},      
        DOUBLE ROOM: {self.DOUBLE},      
        EXECUTIVE ROOM: {self.EXECUTIVE}      
        """

    def __repr__(self):
        return f""" 
        SINGLE ROOM: {self.SINGLE},      
        DOUBLE ROOM: {self.DOUBLE},      
        EXECUTIVE ROOM: {self.EXECUTIVE}      
        """
