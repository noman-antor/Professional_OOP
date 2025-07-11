from appointment import Appointment


class Patient:
    def __init__(self, id: int, name: str, age: str, diseases: str = None, reports: str = None, prescription: str = None):
        self.id = id
        self.name = name
        self.age = age
        self.diseases = diseases
        self.reports = reports
        self.prescription = prescription

    def get_info(self):
        return {
            "id": self.id,
            "name": self.name,
            "age": self.age,
            "diseases": self.diseases,
            "reports": self.reports,
            "prescription": self.prescription
        }
