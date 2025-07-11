from datetime import datetime


class Appointment:
    def __init__(self, from_time: datetime, to_time: datetime, doctor: str, patient_name: str, patient_id: int):
        self.from_time = from_time
        self.to_time = to_time
        self.doctor = doctor
        self.patient_name = patient_name
        self.patient_id = patient_id
