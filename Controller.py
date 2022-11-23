from Model import Patients


class First:
    def __init__(self, model):
        self.model = model

    def find_user(self, my_id):
        pass

    def next_screen(self, my_id):
        if my_id in self.model.id_patient:
            return 0
        elif my_id in self.model.id_doctor:
            return 1
        else:
            pass


class Patient:
    def __init__(self, model):
        self.model = model
        self.id = None
        self.id_doctor = None

    def _find_doctor(self):
        pass

    def find_data(self):
        data = [self.model.full_name_patient, self.model.analysis, self.model.diagnosis]
        return data

    def send_notification(self):
        self._find_doctor()


class Doctor:
    def __init__(self, model):
        self.model = model
        self.id = None
        self.notification = False

    def find_data(self):
        data = [self.model.full_name_doctor, self.model.full_name_patient, self.model.room, self.model.status,
                self.model.analysis, self.model.diagnosis]
        self.id = self.model.id_doctor
        return data

    def edit_status(self, cur_patient, status):
        pass

    def edit_analysis(self, cur_patient, analysis):
        pass

    def edit_diagnosis(self, cur_patient, diagnosis):
        pass

    def get_notification(self, data):
        pass
