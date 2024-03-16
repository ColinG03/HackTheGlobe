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
    def __init__(self, id, total_capacity, num_open_beds, underage = False, only_gender = None, beds = []):
        self.id = id
        self.total_capacity = total_capacity
        self.num_open_beds = num_open_beds
        self.underage = underage
        self.only_gender = only_gender
        self.beds = beds

    def change_status(self, new_status):
        self.status = new_status
    
    def isEmpty(self):
        if self.total_capacity == self.num_open_beds:
            return True
        return False

class Bed:
    def __init__(self, id, category, gender = None, status = BED_STATUS.OPEN):
        self.id = id
        self.category = category
        self.gender = gender
        self.status = status
    
    def change_status(self, new_status):
        self.status = new_status

class Model:
    def __init__(self):
        self.rooms = {'roomA': Room('A', 6, 6, beds=[Bed(1, BED_CATEGORY.BAY), Bed(2, BED_CATEGORY.BAY), Bed(3, BED_CATEGORY.BAY), Bed(4, BED_CATEGORY.BAY), Bed(5, BED_CATEGORY.BAY), Bed(6, BED_CATEGORY.BAY)]),
        'roomB': Room('B', 1, 1, beds=[Bed(7, BED_CATEGORY.SINGLE)]), 
        'roomC': Room('C', 1, 1, beds=[Bed(8, BED_CATEGORY.SINGLE)]), 
        'roomD': Room('D', 1, 1, beds=[Bed(9, BED_CATEGORY.SINGLE)]),
        'roomE': Room('E', 6, 6, beds=[Bed(10, BED_CATEGORY.BAY), Bed(11, BED_CATEGORY.BAY), Bed(12, BED_CATEGORY.BAY), Bed(13, BED_CATEGORY.BAY), Bed(14, BED_CATEGORY.BAY), Bed(15, BED_CATEGORY.BAY)]),
        'roomF': Room('F', 2, 2, beds=[Bed(16, BED_CATEGORY.DOUBLE), Bed(17, BED_CATEGORY.DOUBLE)]),
        'roomG': Room('G', 2, 2, beds=[Bed(18, BED_CATEGORY.DOUBLE), Bed(19, BED_CATEGORY.DOUBLE)]),
        'roomH': Room('H', 1, 1, beds=[Bed(20, BED_CATEGORY.SINGLE)]), 
        'roomI': Room('I', 1, 1, beds=[Bed(21, BED_CATEGORY.SINGLE)])
        }
        self.singleRooms = ['roomB', 'roomC', 'roomD', 'roomH', 'roomI']
        self.bays = ['roomA', 'roomE']
        self.doubleRooms = ['roomF', 'roomG']
        self.patients = []

    def new_patient(self, age, aggressive, gender, cognitive_issues, palliative, contagious, underage, needs_isolation, no_mixed_gender, **kwargs):
        response = self.find_room_bed(underage, gender, needs_isolation, no_mixed_gender)
        if len(response) > 2:
            return response
        else:
            room, bed = response
        patient = Patient(room, bed, age, aggressive, gender, cognitive_issues, palliative, contagious, underage, needs_isolation, no_mixed_gender, **kwargs)
        self.patients.append(patient) #use this list to show a list of all patients and their room if needed
        return patient


    def assignBed(self, bed, room, gender, no_mixed_gender, underage):
        bedChoice = bed.id
        bed.status = BED_STATUS.OCCUPIED
        bed.gender = gender
        if no_mixed_gender:
            self.rooms[room].only_gender = gender
        if underage:
            self.rooms[room].underage = True
        self.rooms[room].num_open_beds -= 1
        return room, bedChoice 

    
    def allSameGenders(self, room, pGender):
        for bed in self.rooms[room].beds:
            print('bed.gender: ')
            print(bed.gender)
            if bed.gender != pGender and bed.gender != None:
                return False
        return True

    def find_room_bed(self, underage, gender, needs_isolation, no_mixed_gender):
        if needs_isolation:
            for room in self.singleRooms:
                if self.rooms[room].num_open_beds > 0:
                    bed = self.rooms[room].beds[0]
                    if bed.status == BED_STATUS.OPEN:
                        return self.assignBed(bed, room, gender, no_mixed_gender, underage) 
            return 'No single rooms available, if the patient is able to be in a shared room, please resubmit with this updated information'

        else:
            if underage:
                if no_mixed_gender:
                    #NOT GOING TO PUT NON-MIXED GENDERS IN A BAY BECAUSE THAT WOULD RESTRICT ANYONE ELSE FROM JOINING THE ROOM THAT ISNT SAME GENDER
                    for room in self.doubleRooms:
                        if self.allSameGenders(room, gender) and (self.rooms[room].underage or self.rooms[room].isEmpty()) and self.rooms[room].num_open_beds > 0:
                            for bed in self.rooms[room].beds:
                                if bed.status == BED_STATUS.OPEN:
                                    return self.assignBed(bed, room, gender, no_mixed_gender, underage)
                    for room in self.singleRooms:
                        if self.rooms[room].num_open_beds > 0: #single room, so not checking for gender, only if available
                            bed = self.rooms[room].beds[0]
                            if bed.status == BED_STATUS.OPEN:
                                return self.assignBed(bed, room, gender, no_mixed_gender, underage) 
                    return 'No non-mixed gender rooms available, if the patient is comfortable with mixed gender rooms, please resubmit with this updated information'
                else:
                    #should underage people be put in bays? and if so, should that restrict adults from being in the same bay?
                    for room in self.bays:
                        if self.rooms[room].num_open_beds > 0 and (self.rooms[room].underage or self.rooms[room].isEmpty()):
                            for bed in self.rooms[room].beds:
                                if bed.status == BED_STATUS.OPEN:
                                    return self.assignBed(bed, room, gender, no_mixed_gender, underage)
                    for room in self.doubleRooms:
                        if self.rooms[room].num_open_beds > 0 and (self.rooms[room].underage or self.rooms[room].isEmpty()):
                            for bed in self.rooms[room].beds:
                                if bed.status == BED_STATUS.OPEN:
                                    return self.assignBed(bed, room, gender, no_mixed_gender, underage)
                    for room in self.singleRooms:
                        if self.rooms[room].num_open_beds > 0:
                            bed = self.rooms[room].beds[0]
                            if bed.status == BED_STATUS.OPEN:
                                return self.assignBed(bed, room, gender, no_mixed_gender, underage) 
                    return 'No rooms available for underage patients'
            else:
                if no_mixed_gender:
                    for room in self.doubleRooms:
                        if self.rooms[room].num_open_beds > 0:
                            if self.allSameGenders(room, gender) and not self.rooms[room].underage:
                                for bed in self.rooms[room].beds:
                                    if bed.status == BED_STATUS.OPEN:
                                        return self.assignBed(bed, room, gender, no_mixed_gender, underage)
                    for room in self.singleRooms:
                        if self.rooms[room].num_open_beds > 0: #single room, so not checking for gender, only if available
                            bed = self.rooms[room].beds[0]
                            if bed.status == BED_STATUS.OPEN:
                                return self.assignBed(bed, room, gender, no_mixed_gender, underage) 
                    return 'No non-mixed gender rooms available, if the patient is comfortable with mixed gender rooms, please resubmit with this updated information'
                else:
                    for room in self.bays:
                        if self.rooms[room].num_open_beds > 0 and not self.rooms[room].underage:
                            for bed in self.rooms[room].beds:
                                if bed.status == BED_STATUS.OPEN:
                                    return self.assignBed(bed, room, gender, no_mixed_gender, underage)
                    for room in self.doubleRooms:
                        if self.rooms[room].num_open_beds > 0 and not self.rooms[room].underage:
                            for bed in self.rooms[room].beds:
                                if bed.status == BED_STATUS.OPEN:
                                    return self.assignBed(bed, room, gender, no_mixed_gender, underage)
                    for room in self.singleRooms:
                        if self.rooms[room].num_open_beds > 0:
                            bed = self.rooms[room].beds[0]
                            if bed.status == BED_STATUS.OPEN:
                                return self.assignBed(bed, room, gender, no_mixed_gender, underage) 
                    return 'No rooms available'

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
