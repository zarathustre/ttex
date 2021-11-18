from PySide6.QtWidgets import QWidget, QHBoxLayout, QTextEdit, QToolButton, QMessageBox, QLabel
from PySide6.QtCore import Slot

from src.uic.player import Ui_Player
from src.network.client import Client
from src.common_tools import add_label, add_horizontal_line, add_tool_button

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
        injects = (label.text() for label in self.player_injects_group.findChildren(QLabel))
        if text not in injects:
            add_label(self.player_injects_group, self.verticalLayout_4, text)
            add_horizontal_line(self.player_injects_group, self.verticalLayout_4)

    @Slot(str)
    def set_question(self, question_text):
        questions = (label.text() for label in self.player_questions_group.findChildren(QLabel))
        if question_text not in questions:
            count = len(self.player_questions_group.findChildren(QToolButton))
            add_label(self.player_questions_group, self.verticalLayout_5, question_text, object_name=f'question_label_{count}')
            self.horizontalLayout = QHBoxLayout()
            answer_text_edit = QTextEdit(self.player_questions_group)
            self.horizontalLayout.addWidget(answer_text_edit)
            send_button = add_tool_button(self.player_questions_group, self.horizontalLayout, text='Submit', return_value=True)
            send_button.clicked.connect(partial(self.send_answer_to_evaluator, question_text, answer_text_edit, send_button))
            self.verticalLayout_5.addLayout(self.horizontalLayout)


    def send_answer_to_evaluator(self, question, answer_text_edit, send_button):
        if answer_text_edit.toPlainText() == '':
            QMessageBox.warning(self, "Warning", "Empty field", QMessageBox.Ok)
        else:
            msg_box = QMessageBox.information(self, "Confirmation", "Are you sure you want to submit your answer ?", QMessageBox.Yes, QMessageBox.No)
            if msg_box == QMessageBox.Yes:
                self.client.send(f'!ANSWER{self.team_nick_label.text()[-1]}{question}!A!{answer_text_edit.toPlainText()}')
                answer_text_edit.clear()
                answer_text_edit.setReadOnly(True)
                send_button.setEnabled(False)
