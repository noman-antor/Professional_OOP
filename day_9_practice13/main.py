from doctor import Doctor
from patient import Patient
from meditation import Meditation
from prescriptions import Prescription

try:
    dr_smith = Doctor("Dr. Smith", "Cardiology")
    patient_john = Patient("John Doe", 30)
    meditation_session = Meditation(
        patient_name=patient_john, doctor_name=dr_smith, dosage=["Anti-Inflammatories","Statins"], frequency=["Daily"]
    )
    Prescription.add_meditation(meditation_session)
    print(Prescription.get_all_meditations())
    print("Meditation session added successfully.")
except ValueError as e:
    print(f"Error: {e}")