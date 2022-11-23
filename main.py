from View import TestApp
from Model import Patients
from Controller import First, Doctor, Patient

class App:
    def __init__(self):
        self.patient = Patients()
        self.first = First(self.patient)
        self.doctor = Doctor(self.patient)
        self.patient_ = Patient(self.patient)
        self.view = TestApp(self.first, self.doctor, self.patient_)

    def create(self):
        self.view.run()

if __name__ == '__main__':
    main = App()
    main.create()
