from PySide6.QtWidgets import QWidget, QLabel, QFrame, QHBoxLayout, QTextEdit, QToolButton
from PySide6.QtCore import Slot

from src.uic.player import Ui_Player
from src.network.client import Client

import threading
from functools import partial


class Player(QWidget, Ui_Player):
    def __init__(self):
        super(Player, self).__init__()
        self.setupUi(self)
        self.init_widgets()
        self.init_connection()
        self.assign_connection_widgets()


    def init_widgets(self):
        self.player_tab.setCurrentIndex(0)


    def init_connection(self):
        self.client = Client()
        self.client_thread = threading.Thread(target=self.client.receive, args=(self.player_time_counter, ), daemon=True)

    def assign_connection_widgets(self):
        self.client.client_signals.scenario_signal.connect(self.set_scenario)
        self.client.client_signals.inject_signal.connect(self.set_inject)
        self.client.client_signals.question_signal.connect(self.set_question)
        self.client.client_signals.team_nick_signal.connect(self.set_team_nickname)

    @Slot(str)
    def set_team_nickname(self, nick):
        self.team_nick_label.setText(f'Team {nick}')

    @Slot(str)
    def set_scenario(self, text):
        self.player_scenario_text.setText(text)

    @Slot(str)
    def set_inject(self, text):
        self.inject_label = QLabel(self.player_injects_group)
        self.inject_label.setText(text)
        self.inject_label.setWordWrap(True)
        self.line = QFrame(self.player_injects_group)
        self.line.setFrameShape(QFrame.HLine)
        self.line.setFrameShadow(QFrame.Sunken)
        self.verticalLayout_4.addWidget(self.inject_label)
        self.verticalLayout_4.addWidget(self.line)

    @Slot(str)
    def set_question(self, text):
        count = len(self.player_questions_group.findChildren(QToolButton))
        self.question_label = QLabel(self.player_questions_group)
        self.question_label.setObjectName(f'question_label_{count}')
        self.question_label.setText(text)
        self.question_label.setWordWrap(True)
        self.verticalLayout_5.addWidget(self.question_label)
        self.horizontalLayout = QHBoxLayout()
        self.answer_text = QTextEdit(self.player_questions_group)
        self.horizontalLayout.addWidget(self.answer_text)
        self.send_answer_button = QToolButton(self.player_questions_group)
        self.send_answer_button.setText('Submit')
        self.horizontalLayout.addWidget(self.send_answer_button)
        self.verticalLayout_5.addLayout(self.horizontalLayout)
        self.send_answer_button.clicked.connect(partial(self.send_answer_to_evaluator, self.question_label, self.answer_text))


    def send_answer_to_evaluator(self, question, answer):
        self.client.send(f'!ANSWER{question.text()}!A!{answer.toPlainText()}')