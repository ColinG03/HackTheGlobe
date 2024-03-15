from enum import Enum

class ROOM_STATUS(Enum):
    OPEN = 1
    OCCUPIED = 2
    CLEANING = 3

class Room:
    def __init__(self, code, status=ROOM_STATUS.OPEN):
        self.code = code
        self.status = status

    def change_status(self, new_status):
        self.status = new_status

class Model:
    def __init__(self):
        self.rooms = {"wingA": {"room1": Room("room1", ROOM_STATUS.OPEN), "room2": Room("room2", ROOM_STATUS.OPEN)}}  # Dictionary to store Room objects, e.g., {"wingA": {"room1": Room("room1", ROOM_STATUS.OPEN)}}

    def new_patient(self, **kwargs):
        patient = Patient(self.find_room(), **kwargs)
        return patient

    def find_room(self):
        # Implement an algorithm to efficiently place patients, put a basic one here for now
        for wing, rooms in self.rooms.items():
            for code, room in rooms.items():
                if room.status == ROOM_STATUS.OPEN:
                    room.change_status(ROOM_STATUS.OCCUPIED)
                    return room
        raise Exception("No rooms available")

    def change_room_status(self, wing, room_code, new_status):
        if wing in self.rooms and room_code in self.rooms[wing]:
            self.rooms[wing][room_code].change_status(new_status)
        else:
            raise Exception("Room not found")

class Patient:
    def __init__(self, room, age, noMixed, aggressive, gender, contagious=False, **kwargs):
        self.room = room
        self.contagious = contagious
        self.age = age
        self.noMixed = noMixed
        self.aggressive = aggressive
        self.gender = gender
        # Add more attributes as needed
        for key, value in kwargs.items():
            setattr(self, key, value)
