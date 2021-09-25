from PySide6.QtWidgets import QWidget
from src.uic.start_scenario_page import Ui_StartScenario
from .evaluator_view import Evaluator


class StartScenario(QWidget, Ui_StartScenario):
    def __init__(self):
        super(StartScenario, self).__init__()
        self.setupUi(self)
        self.init_widgets()
        self.assign_widgets()


    def init_widgets(self):
        self.start_stack.setCurrentIndex(0)


    def assign_widgets(self):
        self.evaluator_button.clicked.connect(lambda: self.create_evaluator())


    def create_evaluator(self):
        self.evaluator = Evaluator()
        self.start_stack.addWidget(self.evaluator)
        self.start_stack.setCurrentIndex(1)    