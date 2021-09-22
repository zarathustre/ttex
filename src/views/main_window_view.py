from PySide6.QtWidgets import QMainWindow
from src.uic.main_window import Ui_MainWindow
from src.views.create_scenario_view import CreateScenario


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setupUi(self)
        self.assign_widgets()
        self.show()


    def assign_widgets(self):
        self.create_scenario_button.clicked.connect(lambda: self.create_scenario())


    def create_scenario(self):
        self.scenario = CreateScenario()
        self.main_stack.addWidget(self.scenario)
        self.main_stack.setCurrentIndex(1)
        self.scenario.back_button.clicked.connect(lambda: clear_and_back())
        self.scenario.create_scenario_tab.currentChanged.connect(lambda: on_tab_change())


        def on_tab_change():
            tab = self.scenario.create_scenario_tab
            next = self.scenario.next_button
            if tab.currentWidget().objectName() == 'tab_3':
                next.setText("Save")
                next.clicked.disconnect()
                next.clicked.connect(lambda: save_and_back())
            else:
                next.setText("Next")
                next.clicked.disconnect()
                next.clicked.connect(lambda: tab.setCurrentIndex(tab.currentIndex() + 1))


        def save_and_back():
            data = self.scenario.get_values()
            print(data)
            clear_and_back()

                
        def clear_and_back():
            self.main_stack.setCurrentIndex(0) 
            self.scenario.deleteLater()
            