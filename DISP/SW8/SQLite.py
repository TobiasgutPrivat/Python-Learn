import sqlite3
# Connect to the SQLite database (it will be created if it doesn't exist)
conn = sqlite3.connect('emr_system.db')
cursor = conn.cursor()
# Create the Patients table
cursor.execute('''CREATE TABLE IF NOT EXISTS Patients (
id INTEGER PRIMARY KEY,
name TEXT NOT NULL,
date_of_birth TEXT NOT NULL,
gender TEXT NOT NULL
)''')
# TODO: Create the MedicalRecords table
# Note 1: The table contains: record_id, patient_id, visit_date, notes
# Note 2: visit_date can be stored as TEXT
# Note 3: Don't forget to reference the patients primary key as a foreign key
cursor.execute('''CREATE TABLE IF NOT EXISTS MedicalRecords (
record_id INTEGER PRIMARY KEY,
patient_id INTEGER NOT NULL,
visit_date TEXT NOT NULL,
notes TEXT NOT NULL,
FOREIGN KEY(patient_id) REFERENCES Patients(id)
)''')
conn.commit()

def add_patient(id, name, date_of_birth, gender):
    cursor.execute("INSERT INTO Patients (id, name, date_of_birth, gender) VALUES (?, ?, ?, ?)", (id, name, date_of_birth, gender))
    conn.commit()

def add_medical_record(record_id, patient_id, visit_date, notes):
    # TODO: insert a medical record
    cursor.execute("INSERT INTO MedicalRecords (record_id, patient_id, visit_date, notes) VALUES (?, ?, ?, ?)", (record_id, patient_id, visit_date, notes))
    conn.commit()

def get_patient_info(patient_id):
    cursor.execute("SELECT * FROM Patients WHERE id=?", (patient_id,))
    return cursor.fetchone()

def get_medical_records_for_patient(patient_id):
    # TODO: Fetch all medical records of a patient.
    # Tip: Use cursor.fetchall()
    cursor.execute("SELECT * FROM MedicalRecords WHERE patient_id=?", (patient_id,))
    return cursor.fetchall()

#Now, let's test the system by adding some patients and medical records, then retrieving them.
# TODO: Add patients
add_patient(1, "John Doe", "1990-01-01", "Male")
add_patient(2, "Jane Doe", "1995-02-02", "Female")
# TODO: Add medical records
add_medical_record(1, 1, "2023-10-01", "Routine check-up")
add_medical_record(2, 2, "2023-10-02", "Follow-up visit")
# TODO: Retrieve and print patient information and medical records
# Uncomment the following lines to see the output
print(get_patient_info(1))
print(get_medical_records_for_patient(1))
# Don't forget to close the connection
conn.close()

