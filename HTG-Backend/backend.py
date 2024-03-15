from flask import Flask, request, jsonify
from flask_cors import CORS 

app = Flask(__name__)
CORS(app, origins=['*'])

@app.route('/', methods=['GET'])
def index():
    return "Welcome to the backend"

@app.route('/patient-info', methods=['GET','POST'])
def process_patient():
    if request.method == 'POST':
        patient_info = request.json
        print(patient_info)

        return jsonify(patient_info)
    else:
        return "method is get"