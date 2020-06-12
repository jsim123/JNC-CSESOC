class Patients:
    def __init__(self, name, gender,email, notes):
        self.name = name
        self.gender = gender
        self.tasks = []
        self.appointments = []
        self.notes = notes
        self.email = email
        self.meds = []
    def add_task(self,task):
        self.tasks.append(task)
    
    def get_name(self):
        return self.name

    def add_appointment(self,appointment):
        self.appointments.append(appointment)

    def get_email(self):
        return self.email

    def get_meds(self):
        return self.meds
    
    def get_appoint_history(self):
        return self.appointments

    def add_medication(self,med):
        self.meds.append(med)