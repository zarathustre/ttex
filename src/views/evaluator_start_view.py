from PySide6.QtWidgets import QWidget, QLabel, QHBoxLayout, QToolButton, QVBoxLayout, QToolBox, QSpinBox
from PySide6.QtCore import QObject, Signal, Slot, QTime

from src.uic.evaluator_start import Ui_EvaluatorStart
from src.network.server import Server
from src.common_tools import add_horizontal_line, add_label, add_tool_button, add_tool_box_page, add_spin_box

import time
import threading
from functools import partial


class EvaluatorSignals(QObject):
    time_signal = Signal(str)


class EvaluatorStart(QWidget, Ui_EvaluatorStart):
    def __init__(self):
        super(EvaluatorStart, self).__init__()
        self.setupUi(self)
        self.init_widgets()
        self.assign_widgets()

        
    def init_widgets(self):
        self.signals = EvaluatorSignals()
        self.evaluator_start_tab.setCurrentIndex(0)
        self.timer_running = True
        self.timer_paused = False

    
    def assign_widgets(self):
        self.start_timer_button.clicked.connect(lambda: self.start_timer_thread())


    def init_connection(self, values):
        self.server = Server()
        self.server_thread = threading.Thread(target=self.server.accept_clients,\
            args=(f"!SCENARIO{values['scenario']}", ), daemon=True)

    
    def assign_connection_widgets(self, values):
        self.server.server_signal.server_signal.connect(self.set_lobby_counter)
        self.server.server_signal.receive_answer_signal.connect(self.receive_answer)
        self.signals.time_signal.connect(self.server.send_time)

        injects = values['injects']
        send_inject_buttons = self.injects_group.findChildren(QToolButton)
        for button in send_inject_buttons:
            i = int(button.objectName()[-1])
            button.clicked.connect(partial(self.server.send_to_all, f'!INJECT{injects[i]}'))

        questions = [q[0] for q in values['qaw']]
        send_question_buttons = self.questions_group.findChildren(QToolButton)
        for button in send_question_buttons:
            i = int(button.objectName()[-1])
            button.clicked.connect(partial(self.server.send_to_all, f'!QUESTION{questions[i]}'))


    def init_answers_tool_box(self):
        self.answers_tool_box = QToolBox(self.tab_3)
        self.answers_tool_box.setObjectName(u"answers_tool_box")
        self.verticalLayout_7.addWidget(self.answers_tool_box)
        self.init_page('Team 0', 'page_team_')


    def init_page(self, title, object_name):
        add_tool_box_page(self.answers_tool_box, title, object_name)
        page = self.answers_tool_box.findChild(QWidget, object_name)
        v_layout = QVBoxLayout(page)
        questions = [label.text() for label in self.questions_group.findChildren(QLabel)]
        for i, q in enumerate(questions):
            add_label(page, v_layout, q, object_name=f'question_label_{i}')
            h_layout = QHBoxLayout()
            v_layout.addLayout(h_layout)
            add_label(page, h_layout, '', size_policy=True, object_name=f'answer_label_{i}')
            add_spin_box(page, h_layout)
            add_horizontal_line(page, v_layout)


    # TODO
    # - Handle the evaluation and scoring of the received answers
    # - Disable send buttons after submission

    @Slot(str)
    def receive_answer(self, msg):
        question_answer = msg.split('!A!')
        nick = question_answer[0][0]
        question = question_answer[0][1:]
        answer = question_answer[1]
        self.update_answer_tab(nick, question, answer)

    
    def update_answer_tab(self, nick, question, answer):

        default_page = self.answers_tool_box.findChild(QWidget, 'page_team_')
        if default_page:
            default_page.setObjectName(f'page_team_{nick}')
            self.answers_tool_box.setItemText(0, f'Team {nick}')

        team_page = self.answers_tool_box.findChild(QWidget, f'page_team_{nick}')
        
        if not team_page:
            self.init_page(f'Team {nick}', f'page_team_{nick}')
            team_page = self.answers_tool_box.findChild(QWidget, f'page_team_{nick}')
            
        for label in team_page.findChildren(QLabel):
            if label.text() == question:
                index = label.objectName()[-1]

        answer_label = team_page.findChild(QLabel, f'answer_label_{index}')
        answer_label.setText(answer)

        
    @Slot(int)
    def set_lobby_counter(self, logged_in):
        self.lobby_counter.display(logged_in)


    def set_timer_false(self):
        self.timer_running = False
        self.timer_paused = False

        
    def start_timer_thread(self):
        timer = self.time_edit.time()
        time_limit = timer.hour() * 3600 + timer.minute() * 60
        if time_limit > 0:
            self.start_timer_button.clicked.disconnect()
            self.start_timer_button.clicked.connect(lambda: self.pause_timer())
            self.start_timer_button.setText('Pause')
        self.time_bar.setMaximum(time_limit)
        self.time_bar.setValue(time_limit)
        thread = threading.Thread(target=self.start_timer, args=(time_limit, ), daemon=True)
        thread.start()
        self.time_edit.setTime(QTime(0,0))


    def pause_timer(self):
        if self.start_timer_button.text() == 'Pause':
            self.timer_paused = True
            self.start_timer_button.setText('Resume')
        elif self.start_timer_button.text() == 'Resume':
            self.timer_paused = False
            self.start_timer_button.setText('Pause')
        

    def start_timer(self, time_limit): 
        self.signals.time_signal.emit(str(time_limit))
        while time_limit >= 0:
            
            if not self.timer_running:
                break

            if self.timer_paused:
                while self.timer_paused:
                    time.sleep(1)

            if time_limit == 0:
                self.time_counter.display(0)
                self.signals.time_signal.emit('0')
                break

            time_limit -= 1
            self.time_bar.setValue(time_limit)                      # TODO: this is raising an error              
            self.time_counter.display((time_limit // 60) + 1)      
            self.signals.time_signal.emit(str(time_limit))
            time.sleep(1)

        print('Done')
            

    def assign_fields(self, dict):
        self.title_label.setText(dict['title'])             # title
        self.scenario_text.setText(dict['scenario'])        # scenario

        # objectives
        add_horizontal_line(self.objectives_group, self.verticalLayout_3)
        for objective in dict['objectives']:
            add_label(self.objectives_group, self.verticalLayout_3, objective)
            add_horizontal_line(self.objectives_group, self.verticalLayout_3)

        # injects
        i = 0
        add_horizontal_line(self.injects_group, self.verticalLayout_5)      
        for inject in dict['injects']:
            horizontalLayout = QHBoxLayout()
            add_label(self.injects_group, horizontalLayout, inject, size_policy=True)
            add_tool_button(self.injects_group, horizontalLayout, text='Send', object_name=f'send_inject_button_{i}')
            self.verticalLayout_5.addLayout(horizontalLayout)
            add_horizontal_line(self.injects_group, self.verticalLayout_5)
            i += 1

        # questions
        i = 0
        add_horizontal_line(self.questions_group, self.verticalLayout_6)
        for qaw in dict['qaw']:
            horizontalLayout = QHBoxLayout()
            add_label(self.questions_group, horizontalLayout, qaw[0], size_policy=True)
            add_tool_button(self.questions_group, horizontalLayout, text='Send', object_name=f'send_question_button_{i}')
            self.verticalLayout_6.addLayout(horizontalLayout)
            add_horizontal_line(self.questions_group, self.verticalLayout_6)
            i += 1
