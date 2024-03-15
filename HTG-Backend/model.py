from enum import Enum

class BED_STATUS(Enum):
    OPEN = 1
    OCCUPIED = 2
    CLEANING = 3

class BED_CATEGORY(Enum):
    SINGLE = 1
    DOUBLE = 2
    BAY = 3

class Room:
    def __init__(self, id, total_capacity, num_open_beds, beds = []):
        self.id = id
        self.total_capacity = total_capacity
        self.num_open_beds = num_open_beds
        self.beds = beds

    def change_status(self, new_status):
        self.status = new_status

class Bed:
    def __init__(self, id, category, status = BED_STATUS.OPEN):
        self.id = id
        self.category = category
        self.status = status
    
    def change_status(self, new_status):
        self.status = new_status

class Model:
    def __init__(self):
        self.rooms = {'roomA': Room('A', 6, 6, [Bed(1, BED_CATEGORY.BAY), Bed(2, BED_CATEGORY.BAY), Bed(3, BED_CATEGORY.BAY), Bed(4, BED_CATEGORY.BAY), Bed(5, BED_CATEGORY.BAY), Bed(6, BED_CATEGORY.BAY)]),
        'roomB': Room('B', 1, 1, [Bed(7, BED_CATEGORY.SINGLE)]), 
        'roomC': Room('C', 1, 1, [Bed(8, BED_CATEGORY.SINGLE)]), 
        'roomD': Room('D', 1, 1, [Bed(9, BED_CATEGORY.SINGLE)]),
        'roomE': Room('E', 6, 6, [Bed(10, BED_CATEGORY.BAY), Bed(11, BED_CATEGORY.BAY), Bed(12, BED_CATEGORY.BAY), Bed(13, BED_CATEGORY.BAY), Bed(14, BED_CATEGORY.BAY), Bed(15, BED_CATEGORY.BAY)]),
        'roomF': Room('F', 2, 2, [Bed(16, BED_CATEGORY.DOUBLE), Bed(17, BED_CATEGORY.DOUBLE)]),
        'roomG': Room('G', 2, 2, [Bed(18, BED_CATEGORY.DOUBLE), Bed(19, BED_CATEGORY.DOUBLE)]),
        'roomH': Room('H', 1, 1, [Bed(20, BED_CATEGORY.SINGLE)]), 
        'roomI': Room('I', 1, 1, [Bed(21, BED_CATEGORY.SINGLE)])
        }
        self.singleRooms = ['roomB', 'roomC', 'roomD', 'roomH', 'roomI']
        self.bays = ['roomA', 'roomE']
        self.doubleRooms = ['roomF', 'roomG']
        self.patients = []

    def new_patient(self, age, aggressive, gender, cognitive_issues, palliative, contagious, underage, needs_isolation, no_mixed_gender, **kwargs):
        room, bed = self.find_room_bed(underage, gender, needs_isolation, no_mixed_gender)
        patient = Patient(room, bed, age, aggressive, gender, cognitive_issues, palliative, contagious, underage, needs_isolation, no_mixed_gender, **kwargs)
        self.patients.append(patient) #use this list to show a list of all patients and their room if needed
        return patient

    # def find_room(self):
    #     # Implement an algorithm to efficiently place patients, put a basic one here for now
    #     for wing, rooms in self.rooms.items():
    #         for code, room in rooms.items():
    #             if room.status == ROOM_STATUS.OPEN:
    #                 room.change_status(ROOM_STATUS.OCCUPIED)
    #                 return room
    #     raise Exception("No rooms available")

    def find_room_bed(self, underage, gender, needs_isolation, no_mixed_gender): # underage, gender, needs_isolation, no_mixed_gender
        if needs_isolation:
            roomChoice = ''
            bedChoice = ''
            for room in self.singleRooms:
                if self.rooms[room].num_open_beds > 0:
                    # for bed in self.rooms[room].beds:     NO NEED FOR THIS BECAUSE ITS SINGLE ROOMS
                    bed = self.rooms[room].beds[0]
                    if bed.status == BED_STATUS.OPEN:
                        bedChoice = bed.id
                        bed.status = BED_STATUS.OCCUPIED
                        roomChoice = room
                        self.rooms[room].num_open_beds -= 1
                        break
        
            return roomChoice, bedChoice 

        else:
            if underage:
                pass #Find room with another underage patient, else find single room
            else:
                if no_mixed_gender:
                    pass #Find room with another patient of the same gender, else find single room
                else:
                    pass #Place patient in any available room, start looking at rooms that already have people in them, only place in empty room (multi or single) if none exist


    def change_room_status(self, wing, room_code, new_status):
        if wing in self.rooms and room_code in self.rooms[wing]:
            self.rooms[wing][room_code].change_status(new_status)
        else:
            raise Exception("Room not found")

class Patient:
    def __init__(self, room, bed, age, aggressive, gender, cognitive_issues, palliative, contagious, underage, needs_isolation, no_mixed_gender, **kwargs):
        self.room = room
        self.bed = bed
        self.contagious = contagious
        self.age = age
        self.noMixed = no_mixed_gender
        self.aggressive = aggressive
        self.gender = gender
        self.cognitive_issues = cognitive_issues
        self.palliative = palliative
        self.underage = underage
        self.needs_isolation = needs_isolation
        # Add more attributes as needed
        for key, value in kwargs.items():
            setattr(self, key, value)
