from flask import Flask, request, jsonify
from flask_cors import CORS 
from model import *

app = Flask(__name__)
CORS(app, origins=['*'])

model = Model()

@app.route('/', methods=['GET'])
def index():
    return "Welcome to the backend"

@app.route('/patient-info', methods=['GET','POST'])
def process_patient():
    if request.method == 'POST':
        patient_info = request.json
        name = patient_info['pName']
        age = patient_info['pAge']
        gender = patient_info['pGender']
        palliative = patient_info['isoPalliative']
        contagious = patient_info['isoContagious']
        aggressive = patient_info['superAgg']
        cognitive_issues = patient_info['superCog']
        no_mixed_gender = patient_info['noMixedReligious']
        if type(no_mixed_gender) == type(""):
            if no_mixed_gender == 'false':
                no_mixed_gender = False
            else:
                no_mixed_gender = True

        if type(palliative) == type(""):
            if palliative == 'false':
                palliative = False
            else:
                palliative = True

        if type(aggressive) == type(""):
            if aggressive == 'false':
                aggressive = False
            else:
                aggressive = True

        if type(contagious) == type(""):
            if contagious == 'false':
                contagious = False
            else:
                contagious = True

        print('palliative')
        print(palliative)
        print('aggressive')
        print(aggressive)
        print('contagious')
        print(contagious)

        underage = False
        if int(age) < 18:
            underage = True
        
        needs_isolation = False
        if palliative or aggressive or contagious:
            needs_isolation = True
        print('needs isolation')
        print(needs_isolation)
        
        # patient should have all traits and derived traits
        newPatient = model.new_patient(age, aggressive, gender, cognitive_issues, palliative, contagious, underage, needs_isolation, no_mixed_gender)
        if type(newPatient) != Patient:
            return newPatient
        print(newPatient.room, newPatient.bed, newPatient.age)
        return jsonify({'room': newPatient.room, 'bed': newPatient.bed})
    else:
        return "method is get"

@app.route('/free-bed', methods=['GET', 'POST'])
def free_bed():
    if request.method == 'POST':
        #Hardcoding this because its 2am and its due tomorrow... oops
        bed_to_free = request.json
        if bed_to_free <= 6:
            room = model.rooms['roomA']
            room.beds[bed_to_free-1].status = BED_STATUS.OPEN
            room.num_open_beds += 1
            if room.isEmpty():
                room.only_gender = None
                room.underage = False
        elif bed_to_free == 7:
            room = model.rooms['roomB']
            room.beds[0].status = BED_STATUS.OPEN
            room.num_open_beds += 1
            if room.isEmpty():
                room.only_gender = None
                room.underage = False
        elif bed_to_free == 8:
            room = model.rooms['roomC']
            room.beds[0].status = BED_STATUS.OPEN
            room.num_open_beds += 1
            if room.isEmpty():
                room.only_gender = None
                room.underage = False
        elif bed_to_free == 9:
            room = model.rooms['roomD']
            room.beds[0].status = BED_STATUS.OPEN
            room.num_open_beds += 1
            if room.isEmpty():
                room.only_gender = None
                room.underage = False
        elif bed_to_free <= 15:
            room = model.rooms['roomE']
            room.beds[bed_to_free-10].status = BED_STATUS.OPEN
            room.num_open_beds += 1
            if room.isEmpty():
                room.only_gender = None
                room.underage = False
        elif bed_to_free <= 17:
            room = model.rooms['roomF']
            room.beds[bed_to_free-16].status = BED_STATUS.OPEN
            room.num_open_beds += 1
            print(room.total_capacity, room.num_open_beds)
            if room.isEmpty():
                print('isempty')
                room.only_gender = None
                room.underage = False
        elif bed_to_free <= 19:
            room = model.rooms['roomG']
            room.beds[bed_to_free-18].status = BED_STATUS.OPEN
            room.num_open_beds += 1
            if room.isEmpty():
                room.only_gender = None
                room.underage = False
        elif bed_to_free == 20:
            room = model.rooms['roomH']
            room.beds[0].status = BED_STATUS.OPEN
            room.num_open_beds += 1
            if room.isEmpty():
                room.only_gender = None
                room.underage = False
        elif bed_to_free == 21:
            room = model.rooms['roomI']
            room.beds[0].status = BED_STATUS.OPEN
            room.num_open_beds += 1
            if room.isEmpty():
                room.only_gender = None
                room.underage = False
        return 'Bed status updated successfully'
    else:
        return 'Method is get'