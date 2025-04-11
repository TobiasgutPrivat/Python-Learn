import TinyDB

from tinydb import TinyDB, Query
# Initialize the TinyDB database
db = TinyDB('emr_system.json')
patients = db.table('Patients')
# TODO: Add the table MedicalRecords    
medical_records = db.table('MedicalRecords')

def add_patient(patient_id, name, date_of_birth, gender):
    patients.insert({
    'id': patient_id,
    'name': name,
    'date_of_birth': date_of_birth,
    'gender': gender
    })

def add_medical_record(record_id, patient_id, visit_date, notes):
    # TODO: Add a medical record
    medical_records.insert({
    'record_id': record_id,
    'patient_id': patient_id,
    'visit_date': visit_date,
    'notes': notes
    })

def get_patient_info(patient_id):
    patient = Query()
    return patients.search(patient.id == patient_id)

def get_medical_records_for_patient(patient_id):
    # TODO: Get all medical records for a patient
    record = Query()
    return medical_records.search(record.patient_id == patient_id)

# TODO: Add patients
add_patient(1, "John Doe", "1990-01-01", "Male")
add_patient(2, "Jane Doe", "1995-02-02", "Female")
# TODO: Add medical records
add_medical_record(1, 1, "2023-10-01", "Routine check-up")
add_medical_record(2, 2, "2023-10-02", "Follow-up visit")
# TODO: Retrieve and display patient information and medical records
print(get_patient_info(1))
print(get_medical_records_for_patient(1))