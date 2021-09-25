from PySide6.QtWidgets import QMainWindow, QMessageBox
from src.uic.main_window import Ui_MainWindow
from .create_scenario_view import CreateScenario
from .start_scenario_view import StartScenario
import threading


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setupUi(self)
        self.assign_widgets()
        self.show()


    def assign_widgets(self):
        self.create_scenario_button.clicked.connect(lambda: self.create_scenario())
        self.start_scenario_button.clicked.connect(lambda: self.start_scenario())


    def start_scenario(self):
        self.start_scenario_obj = StartScenario()
        self.main_stack.addWidget(self.start_scenario_obj)
        self.main_stack.setCurrentIndex(1)

        # assign widgets
        self.start_scenario_obj.back_button.clicked.connect(lambda: clear_and_back())

        # TODO fix the back button functionality to be more dynamic by changing to the previous page instead of home page

        def clear_and_back():
            self.main_stack.setCurrentIndex(0)
            self.start_scenario_obj.deleteLater()


    # Handles the creation of a new scenario
    def create_scenario(self):
        self.create_scenario_obj = CreateScenario()              # create scenario object
        self.main_stack.addWidget(self.create_scenario_obj)      # add object to main stack
        self.main_stack.setCurrentIndex(1)                       # switch main stack to show created object

        # assign widgets
        self.create_scenario_obj.back_button.clicked.connect(lambda: clear_and_back())     # back button
        self.create_scenario_obj.create_scenario_tab.currentChanged.connect(\
            lambda: self.create_scenario_obj.on_tab_change(save_and_back))                 # tabbed widget

        # Change the main stack to the first one and delete the create scenario object
        def clear_and_back():
            self.main_stack.setCurrentIndex(0) 
            self.create_scenario_obj.deleteLater()         # delete create scenario object

        # Save entries of the create scenario in the database
        def save_and_back():
            if self.create_scenario_obj.check_constraints():
                thread = threading.Thread(target=self.create_scenario_obj.save_to_db())
                thread.start()
                clear_and_back()
