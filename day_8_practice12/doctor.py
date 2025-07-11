from appointment import Appointment
from patient import Patient


class Doctor:
    max_patients = 2
    __patients = []
    appointments = []

    def __init__(self, doctors_name: str, speciality: str, chamber_no: int):
        self.doctors_name = doctors_name
        self.speciality = speciality
        self.chamber_no = chamber_no

    def add_patient(self, patient: Patient):
        if len(self.__patients) <= self.max_patients:
            self.__patients.append(patient)
        else:
            raise Exception("Maximum number of patients reached")
 
    def get_patients(self):
        return [
            {
                "name": patient.name,
                "age": patient.age,
                "diseases": patient.diseases
            }
            for patient in self.__patients
        ]

    def set_appointments(self, appointment: Appointment):
        self.appointments.append(appointment)
 
    def get_patient_appointment(self, patient: Patient):
        for appointment in self.appointments:
            if appointment.patient_id == patient.id:
                return {
                    "from_time": appointment.from_time,
                    "to_time": appointment.to_time,
                    "doctor": appointment.doctor,
                    "patient_name": appointment.patient_name,
                    "patient_id": appointment.patient_id
                }
            else:
                raise Exception("Appointment not found for this patient")

    def view_all_appointments(self):
        return [
            {
                "from_time": appointment.from_time,
                "to_time": appointment.to_time,
                "doctor": appointment.doctor,
                "patient_name": appointment.patient_name,
                "patient_id": appointment.patient_id
            }
            for appointment in self.appointments
        ]

    def diagnosis(self, status: str, patient: Patient):
        if patient not in self.__patients:
            raise Exception("Patient not found")
        patient.diseases = status
        patient.reports = f"Reports for {status} "
        return f"Diagnosis for {patient.name}: {status}"

    def prescribe(self, prescription: str, patient: Patient):
        if patient not in self.__patients:
            raise Exception("Patient not found")
        patient.prescription = prescription
        return f"Prescription for {patient.name}: {prescription}"

    def close_appointment(self, patient: Patient):
        if patient not in self.__patients:
            raise Exception("Patient not found")
        for appointment in self.appointments:
            if appointment.patient_id == patient.id:
                self.appointments.remove(appointment)
                break
        self.__patients.remove(patient)
        return f"Appointment closed for {patient.name}"
