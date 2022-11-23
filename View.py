import os.path

from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.core.window import Window
from kivy.config import Config

Config.set('graphics', 'resizable', False)
Config.set('graphics', 'width', '350')
Config.set('graphics', 'height', '550')

Builder.load_file(os.path.join(os.path.dirname(__file__), "ui.kv"))


class FirstScreen(Screen):

    def __init__(self, controller):
        super(FirstScreen, self).__init__()
        self.controller = controller
        self.my_id = None

    def read_id(self, id_txt):
        self.my_id = id_txt
        self.controller.find_user(self.my_id)

    def show_screen(self):
        switch = self.controller.next_screen(self.my_id)
        if switch == 1:
            self.manager.transition.direction = 'left'
            self.manager.current = 'doctor'

        elif switch == 0:
            self.manager.transition.direction = 'left'
            self.manager.current = 'patient'
        else:
            pass


class DoctorScreen(Screen):
    def __init__(self, controller):
        super(DoctorScreen, self).__init__(name='doctor')
        self.controller = controller
        self.id = None
        self.cur_patient = None
        self.show()

    def read_patient(self, text):
        self.cur_patient = text

    def read_status(self, text):
        self.controller.edit_status(self.cur_patient, text)

    def read_analysis(self, text):
        self.controller.edit_analysis(self.cur_patient, text)

    def read_diagnosis(self, text):
        self.controller.edit_diagnosis(self.cur_patient, text)

    def show_notification(self):
        pass

    def _save(self):
        pass

    def show(self):
        self.ids['id_hello'].text = f"Привет, {self.controller.find_data()[0]}!"
        self.ids['id_name'].text = self.controller.find_data()[1]
        self.ids['id_room'].text = self.controller.find_data()[2]
        self.ids['id_status'].text = self.controller.find_data()[3]


class PatientScreen(Screen):
    def __init__(self, controller):
        super(PatientScreen, self).__init__(name='patient')
        self.controller = controller
        self.id = None
        self.show()

    def show(self):
        self.ids['id_hello'].text = f"Привет, {self.controller.find_data()[0]}!"
        self.ids['id_date'].text = f"11.11.2022"

    def show_time_table_screen(self):
        self.manager.transition.direction = 'left'
        self.manager.current = 'timetable'

    def show_analysis_screen(self):
        self.manager.transition.direction = 'left'
        self.manager.current = 'analysis'

    def show_diagnosis_screen(self):
        self.manager.transition.direction = 'left'
        self.manager.current = 'diagnosis'

    def send_notification(self):
        self.controller.send_notification()


class PatientTimeTableScreen(Screen):
    def __init__(self, controller):
        super(PatientTimeTableScreen, self).__init__(name='timetable')
        self.controller = controller

    def send_notification(self):
        PatientScreen.send_notification(self)


class PatientAnalysisScreen(Screen):
    def __init__(self, controller):
        super(PatientAnalysisScreen, self).__init__(name='analysis')
        self.controller = controller

    def send_notification(self):
        PatientScreen.send_notification(self)


class PatientDiagnosisScreen(Screen):
    def __init__(self, controller):
        super(PatientDiagnosisScreen, self).__init__(name='diagnosis')
        self.controller = controller

    def send_notification(self):
        PatientScreen.send_notification(self)


class TestApp(App):
    def __init__(self, first, doctor, patient):
        super(TestApp, self).__init__()
        self.first = first
        self.doctor = doctor
        self.patient = patient

    Window.clearcolor = (255, 255, 255, 1)

    def build(self):
        self.title = "OnTime"
        sm = ScreenManager()
        sm.add_widget(FirstScreen(self.first))
        sm.add_widget(DoctorScreen(self.doctor))
        sm.add_widget(PatientScreen(self.patient))
        sm.add_widget(PatientTimeTableScreen(self.patient))
        sm.add_widget(PatientAnalysisScreen(self.patient))
        sm.add_widget(PatientDiagnosisScreen(self.patient))
        return sm
