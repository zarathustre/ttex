from PySide6.QtWidgets import QWidget
from src.uic.start_scenario_page import Ui_StartScenario


class StartScenario(QWidget, Ui_StartScenario):
    def __init__(self):
        super(StartScenario, self).__init__()
        self.setupUi(self)
        self.init_widgets()
        self.assign_widgets()


    def init_widgets(self):
        self.start_stack.setCurrentIndex(0)


    def assign_widgets(self):
        pass


    # Handles the stack change in the start scenario page
    def on_tab_change(self, clear_and_back):
        stack = self.start_stack
        back = self.back_button
        if stack.currentIndex() == 0:        
            back.clicked.disconnect()
            back.clicked.connect(lambda: clear_and_back())    
        else:
            back.clicked.disconnect()
            back.clicked.connect(lambda: stack.setCurrentIndex(stack.currentIndex() - 1))
