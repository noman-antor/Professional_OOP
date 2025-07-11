from patient import Patient
from doctor import Doctor
from datetime import datetime
from appointment import Appointment

try:
    dr_smith = Doctor("Dr. Smith", "Cardiology", 101)
    patient1 = Patient(1, "John Doe", "30")
    dr_smith.add_patient(patient1)
    
    '''Adding appointments'''
    dr_smith.set_appointments(
        Appointment(
            from_time=datetime(2023, 10, 1, 9, 0),
            to_time=datetime(2023, 10, 1, 10, 0),
            doctor=dr_smith.doctors_name,
            patient_name=patient1.name,
            patient_id=patient1.id
        ))

    print(patient1.get_info())
    print(dr_smith.get_patient_appointment(patient1))

    dr_smith.diagnosis("Healthy", patient1)
    dr_smith.prescribe("Take vitamin D", patient1)
    print(dr_smith.close_appointment(patient1))
    print(patient1.get_info())
    print(dr_smith.get_patient_appointment(patient1))

    print(dr_smith.view_all_appointments())


except Exception as e:
    print(f"An error occurred: {e}")