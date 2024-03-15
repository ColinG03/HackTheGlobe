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

        underage = False
        if float(age) < 18:
            underage = True
        
        needs_isolation = False
        if palliative or aggressive or contagious:
            needs_isolation = True

        # patient should have all traits and derived traits
        newPatient = model.new_patient(age, aggressive, gender, cognitive_issues, palliative, contagious, underage, needs_isolation, no_mixed_gender)
        print(newPatient.room, newPatient.bed, newPatient.age)
        return 'works?'
    else:
        return "method is get"