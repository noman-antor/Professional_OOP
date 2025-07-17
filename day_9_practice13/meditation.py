from doctor import Doctor
from patient import Patient

invalid_combinations = [
    ("Antibiotics", "Statins"),
    ("Muscle Relaxants", "CNS Depressants"),
    ("Anti-Inflammatories", "Anticoagulants")
]


class Meditation:

    def __init__(self, patient_name: Patient, doctor_name: Doctor, dosage: list, frequency: list):
        self.patient_name = patient_name
        self.doctor_name = doctor_name

        for combo in invalid_combinations:
            if all(med in dosage for med in combo):
                raise ValueError(f"Invalid combination: {combo[0]} and {combo[1]} cannot be prescribed together")
    
        self.dosage = dosage
        self.frequency = frequency

