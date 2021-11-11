from PySide6.QtWidgets import QWidget, QLabel, QFrame, QHBoxLayout, QSizePolicy, QToolButton, QGroupBox, QVBoxLayout
from PySide6.QtCore import QObject, Signal, Slot, QTime

from src.uic.evaluator_start import Ui_EvaluatorStart
from src.network.server import Server

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
        for label in self.tab_3.findChildren(QLabel):
            if label.text() == question:
                index = label.objectName()[-1]

        for group in self.tab_3.findChildren(QGroupBox):
            if group.objectName()[-1] == index:
                layout = group.findChildren(QVBoxLayout)[0]
                self.add_label(group, layout, f'Team {nick}: {answer}')
                self.add_horizontal_line(group, layout)   

        
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
        self.add_horizontal_line(self.objectives_group, self.verticalLayout_3)
        for objective in dict['objectives']:
            self.add_label(self.objectives_group, self.verticalLayout_3, objective)
            self.add_horizontal_line(self.objectives_group, self.verticalLayout_3)

        # injects
        i = 0
        self.add_horizontal_line(self.injects_group, self.verticalLayout_5)      
        for inject in dict['injects']:
            horizontalLayout = QHBoxLayout()
            self.add_label(self.injects_group, horizontalLayout, inject, True)
            self.add_tool_button(self.injects_group, horizontalLayout, f'send_inject_button_{i}', 'Send')
            self.verticalLayout_5.addLayout(horizontalLayout)
            self.add_horizontal_line(self.injects_group, self.verticalLayout_5)
            i += 1

        # questions
        i = 0
        self.add_horizontal_line(self.questions_group, self.verticalLayout_6)
        for qaw in dict['qaw']:
            horizontalLayout = QHBoxLayout()
            self.add_label(self.questions_group, horizontalLayout, qaw[0], size_policy=True)
            self.add_tool_button(self.questions_group, horizontalLayout, f'send_question_button_{i}', 'Send')
            self.verticalLayout_6.addLayout(horizontalLayout)
            self.add_horizontal_line(self.questions_group, self.verticalLayout_6)

            # tab 3 questions
            self.add_label(self.tab_3, self.verticalLayout_7, qaw[0], object_name=f'eval_question_label_{i}')
            questions_answers_group = QGroupBox(self.tab_3)
            questions_answers_group.setObjectName(f"questions_answers_group_{i}")
            v_layout = QVBoxLayout(questions_answers_group)
            self.verticalLayout_7.addWidget(questions_answers_group)

            i += 1


    def add_horizontal_line(self, parent, parent_layout):
        line = QFrame(parent)
        line.setFrameShape(QFrame.HLine)
        line.setFrameShadow(QFrame.Sunken)
        parent_layout.addWidget(line)

    def add_label(self, parent, parent_layout, label_text, size_policy=False, object_name=''):
        label = QLabel(parent)
        if size_policy:
            self.add_size_policy(label)
        if object_name != '':
            label.setObjectName(object_name)
        label.setText(label_text)
        label.setWordWrap(True)
        parent_layout.addWidget(label)

    def add_size_policy(self, label):
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(label.sizePolicy().hasHeightForWidth())
        label.setSizePolicy(sizePolicy)

    def add_tool_button(self, parent, parent_layout, object_name, button_text):
        t_button = QToolButton(parent)
        t_button.setObjectName(object_name)
        t_button.setText(button_text)
        parent_layout.addWidget(t_button)