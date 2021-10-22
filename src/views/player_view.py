from PySide6.QtWidgets import QWidget, QLabel, QFrame, QHBoxLayout, QTextEdit, QToolButton
from src.uic.player import Ui_Player
from PySide6.QtCore import Slot, Signal, QObject


class PlayerSignals(QObject):
    inject_signal = Signal(str)
    question_signal = Signal(str)
    scenario_signal = Signal(str)


class Player(QWidget, Ui_Player):
    def __init__(self):
        super(Player, self).__init__()
        self.setupUi(self)
        self.init_signals()


    def init_signals(self):
        self.signals = PlayerSignals()
        self.signals.inject_signal.connect(self.set_inject)
        self.signals.question_signal.connect(self.set_question)
        self.signals.scenario_signal.connect(self.set_scenario)


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
        self.question_label = QLabel(self.player_questions_group)
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

    
    @Slot(str)
    def set_scenario(self, text):
        self.player_scenario_text.setText(text)
