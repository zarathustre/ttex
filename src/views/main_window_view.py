from PySide6.QtWidgets import QMainWindow

from src.uic.main_window import Ui_MainWindow
from .create_scenario_view import CreateScenario
from .start_scenario_view import StartScenario
from .evaluator_view import Evaluator
from .evaluator_start_view import EvaluatorStart
from .player_view import Player

import threading


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setupUi(self)
        self.assign_widgets()
        self.show()

    def closeEvent(self, event):
        if hasattr(self, 'start_evaluator_scenario_obj'): 
            self.start_evaluator_scenario_obj.server.shutdown_server()
        elif hasattr(self, 'player'): 
            self.player.client.shutdown_client()
        event.accept()

    def assign_widgets(self):
        self.create_scenario_button.clicked.connect(lambda: self.create_scenario())
        self.start_scenario_button.clicked.connect(lambda: self.start_scenario())

    def start_scenario(self):
        self.start_scenario_obj = StartScenario()
        self.add_widget_and_change_tab(self.main_stack, self.start_scenario_obj, 1)
        self.assign_start_scenario_widgets()

    def assign_start_scenario_widgets(self):
        self.start_scenario_obj.back_button.clicked.connect(lambda: self.delete_objects_and_go_back(self.start_scenario_obj))
        self.start_scenario_obj.evaluator_button.clicked.connect(lambda: self.create_evaluator())
        self.start_scenario_obj.player_button.clicked.connect(lambda: self.create_player())
        self.start_scenario_obj.start_stack.currentChanged.connect(\
            lambda: self.start_scenario_obj.on_tab_change(\
                lambda: self.delete_objects_and_go_back(self.start_scenario_obj)))

    def create_evaluator(self):
        self.evaluator_obj = Evaluator()
        self.add_widget_and_change_tab(self.start_scenario_obj.start_stack, self.evaluator_obj, 1)
        self.assign_create_evaluator_widgets()

    def assign_create_evaluator_widgets(self):
        self.evaluator_obj.create_from_start_button.clicked.connect(lambda: self.create_scenario_from_evaluator())
        self.evaluator_obj.start_button.clicked.connect(lambda: self.start_evaluator_scenario())
        
    def create_scenario_from_evaluator(self):
        self.create_scenario()
        self.delete_objects(self.evaluator_obj, self.start_scenario_obj)
    
    def start_evaluator_scenario(self):
        self.start_evaluator_scenario_obj = EvaluatorStart()
        self.add_widget_and_change_tab(self.main_stack, self.start_evaluator_scenario_obj, 2)
        self.init_start_evaluator_scenario()

    def init_start_evaluator_scenario(self):
        self.start_evaluator_scenario_obj.terminate_button.clicked.connect(lambda: self.terminate_evaluator())
        values = self.evaluator_obj.get_from_db()
        if values: 
            self.start_evaluator_scenario_obj.assign_fields(values)       
            self.start_evaluator_scenario_obj.init_connection(values)
            self.start_evaluator_scenario_obj.server_thread.start()
            self.start_evaluator_scenario_obj.assign_connection_widgets(values)
            self.start_evaluator_scenario_obj.init_answers_tool_box()

    def terminate_evaluator(self):
        self.start_evaluator_scenario_obj.server.shutdown_server()
        self.start_evaluator_scenario_obj.set_timer_false()
        self.delete_objects_and_go_back(self.start_evaluator_scenario_obj, self.evaluator_obj, self.start_scenario_obj)

    def create_player(self):
        self.player = Player()
        self.add_widget_and_change_tab(self.main_stack, self.player, 2)
        self.player.player_terminate_button.clicked.connect(lambda: self.terminate_player())
        self.player.client_thread.start()

    def terminate_player(self):
        self.player.client.shutdown_client()
        self.delete_objects_and_go_back(self.player, self.start_scenario_obj)

    def create_scenario(self):
        self.create_scenario_obj = CreateScenario() 
        self.add_widget_and_change_tab(self.main_stack, self.create_scenario_obj, 1)                     

        self.create_scenario_obj.back_button.clicked.connect(\
            lambda: self.delete_objects_and_go_back(self.create_scenario_obj))

        self.create_scenario_obj.create_scenario_tab.currentChanged.connect(\
            lambda: self.create_scenario_obj.on_tab_change(self.save_delete_go_back))     

    def save_delete_go_back(self):
        if self.create_scenario_obj.check_constraints():
            thread = threading.Thread(target=self.create_scenario_obj.save_to_db)
            thread.start()
            self.delete_objects_and_go_back(self.create_scenario_obj)

    def delete_objects_and_go_back(self, *args):
        self.main_stack.setCurrentIndex(0)
        self.delete_objects(*args)

    def delete_objects(self, *args):
        for arg in args:
            arg.deleteLater()

    def add_widget_and_change_tab(self, stack, widget, tab):
        stack.addWidget(widget)
        stack.setCurrentIndex(tab)