from flask_login import UserMixin
class Doctor(UserMixin):
    def __init__(self,name , username, password):
        self.patients = []
        self.name = name
        self.username = username
        self.password = password
        self.id = 1
    def add_patients(self,patient):
        self.patients.append(patient)

    def check_login_credentials(self,username,password):
        return (self.username == username and self.password == password)
    
    def get_id(self):
        return self.username
    
    def get_patients(self):
        return self.patients

    def get_patient(self,patient):
        for person in self.patients:
            if person.name == patient:
                return person
        return None

    def add_appointment(self,date,doctor_tasks,meds,notes,patient):
        appointment = Appointment(date,self.name,doctor_tasks,meds,notes)
        patient.add_appointment(Appointment)
