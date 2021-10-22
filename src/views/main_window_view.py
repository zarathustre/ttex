from PySide6.QtWidgets import QMainWindow, QToolButton
from src.uic.main_window import Ui_MainWindow
from .create_scenario_view import CreateScenario
from .start_scenario_view import StartScenario
from .evaluator_view import Evaluator
from .evaluator_start_view import EvaluatorStart
from .player_view import Player
import threading
from functools import partial
from src.network.server import Server
from src.network.client import Client


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
        self.start_scenario_obj.evaluator_button.clicked.connect(lambda: create_evaluator())
        self.start_scenario_obj.start_stack.currentChanged.connect(lambda: self.start_scenario_obj.on_tab_change(clear_and_back))
        self.start_scenario_obj.player_button.clicked.connect(lambda: create_player())


        def clear_and_back():
            self.main_stack.setCurrentIndex(0)
            self.start_scenario_obj.deleteLater()


        def create_evaluator():
            evaluator_obj = Evaluator()
            self.start_scenario_obj.start_stack.addWidget(evaluator_obj)  
            self.start_scenario_obj.start_stack.setCurrentIndex(1)
            evaluator_obj.create_from_start_button.clicked.connect(lambda: create_from_start())
            evaluator_obj.start_button.clicked.connect(lambda: evaluator_start())
            

            def create_from_start():
                self.create_scenario()
                evaluator_obj.deleteLater()
                self.start_scenario_obj.deleteLater()

        
            def evaluator_start():
                evaluator_start_obj = EvaluatorStart()
                self.main_stack.addWidget(evaluator_start_obj)
                self.main_stack.setCurrentIndex(2)

                evaluator_start_obj.terminate_button.clicked.connect(lambda: clear_all_back())

                values = evaluator_obj.get_from_db()
                if values:
                    evaluator_start_obj.assign_fields(values)
                
                server = Server()
                server_thread = threading.Thread(target=server.accept_clients,\
                    args=(f"!SCENARIO{values['scenario']}", ), daemon=True)
                server_thread.start()

                server.server_signal.server_signal.connect(evaluator_start_obj.set_lobby_counter)
                evaluator_start_obj.time_signal.time_signal.connect(server.send_time)

                injects = values['injects']
                send_inject_buttons = evaluator_start_obj.injects_group.findChildren(QToolButton)
                for button in send_inject_buttons:
                    i = int(button.objectName()[-1])
                    button.clicked.connect(partial(server.send_to_all, f'!INJECT{injects[i]}'))

                questions = [q[0] for q in values['qaw']]
                send_question_buttons = evaluator_start_obj.questions_group.findChildren(QToolButton)
                for button in send_question_buttons:
                    i = int(button.objectName()[-1])
                    button.clicked.connect(partial(server.send_to_all, f'!QUESTION{questions[i]}'))

                def clear_all_back():
                    server.shutdown_server()
                    evaluator_start_obj.timer_running = False
                    evaluator_start_obj.timer_paused = False
                    self.main_stack.setCurrentIndex(0)
                    evaluator_start_obj.deleteLater()
                    evaluator_obj.deleteLater()
                    self.start_scenario_obj.deleteLater()


        # TODO: reset time edit when the timer is started
        # TODO: send back the answers for every question
        # TODO: adjust number of logged in clients when a client disconnects
        def create_player():
            player = Player()
            self.main_stack.addWidget(player)
            self.main_stack.setCurrentIndex(2)
            player.player_tab.setCurrentIndex(0)
            player.player_terminate_button.clicked.connect(lambda: terminate_player())

            client = Client()
            client_thread = threading.Thread(target=client.receive,\
                args=(player.signals.inject_signal, player.signals.question_signal, player.signals.scenario_signal,\
                    player.player_time_counter, ), daemon=True)
            client_thread.start()

            def terminate_player():
                client.shutdown_client()
                self.main_stack.setCurrentIndex(0)
                player.deleteLater()
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

        # Save entries of the create scenario in the database
        def save_and_back():
            if self.create_scenario_obj.check_constraints():
                thread = threading.Thread(target=self.create_scenario_obj.save_to_db)
                thread.start()
                clear_and_back()

        # Change the main stack to the first one and delete the create scenario object
        def clear_and_back():
            self.main_stack.setCurrentIndex(0) 
            self.create_scenario_obj.deleteLater()         # delete create scenario object
