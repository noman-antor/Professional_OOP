from meditation import Meditation
from doctor import Doctor
from patient import Patient


class Prescription:

    meditation = []

    @classmethod
    def add_meditation(cls, meditation: Meditation):
        cls.meditation.append(meditation)

    @classmethod
    def get_all_meditations(cls):
        return [
            {
                "patient_name": meditation.patient_name,
                "doctor_name": meditation.doctor_name,
                "dosage": meditation.dosage,
                "frequency": meditation.frequency
            } for meditation in cls.meditation
        ]

    @classmethod
    def get_meditation_by_patient(cls, patient: Patient):
        for med in cls.meditation:
            if med.patient_name == patient:
                return {
                    "patient_name": med.patient_name,
                    "doctor_name": med.doctor_name,
                    "dosage": med.dosage,
                    "frequency": med.frequency
                }
        return None

    @classmethod
    def get_meditation_by_doctor(cls, doctor: Doctor):
        for med in cls.meditation:
            if med.doctor_name == doctor.name:
                return {
                    "patient_name": med.patient_name,
                    "doctor_name": med.doctor_name,
                    "dosage": med.dosage,
                    "frequency": med.frequency
                }
        return None

