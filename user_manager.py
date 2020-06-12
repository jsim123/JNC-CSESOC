from doctors import Doctor
from patients import Patients
from appointments import Appointment
class UserManager(object):
    def __init__(self):
        #also adding dummy data
        doctor = Doctor("Turnip Cow","christine lu","nina chen")
        patient1 = Patients("Nina Chen", "Male","carrotcow@gmail.com", "SWAG")
        patient2 = Patients("Christine Lu", "Female","tomatocow@gmail.com", "COOL")
        patient1.add_medication("Weed")
        patient1.add_task("Run 100km")
        patient2.add_medication("Cigs")
        patient2.add_task("Run 100km")
        patient1.add_appointment(Appointment("05/05/2020","panadol","just a mild fever"))
        doctor.add_patients(patient1)
        doctor.add_patients(patient2)
        self.users = [doctor]
    
    def verify(self,username,password):
        for user in self.users:
            if user.check_login_credentials(username,password):
                return True
        return False
    
    def get_user(self,username):
        for user in self.users:
            if user.username == username:
                return user
