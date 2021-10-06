from PySide6.QtWidgets import QWidget, QLabel, QFrame, QHBoxLayout, QSizePolicy, QToolButton
from src.uic.evaluator_start import Ui_EvaluatorStart
import time
import threading


class EvaluatorStart(QWidget, Ui_EvaluatorStart):
    def __init__(self):
        super(EvaluatorStart, self).__init__()
        self.setupUi(self)
        self.init_widgets()
        self.assign_widgets()
        
    
    def init_widgets(self):
        self.evaluator_start_tab.setCurrentIndex(0)
        self.timer_running = True
        self.timer_paused = False
    
    
    def assign_widgets(self):
        self.start_timer_button.clicked.connect(lambda: self.start_timer_thread())


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


    def pause_timer(self):
        if self.start_timer_button.text() == 'Pause':
            self.timer_paused = True
            self.start_timer_button.setText('Resume')
        elif self.start_timer_button.text() == 'Resume':
            self.timer_paused = False
            self.start_timer_button.setText('Pause')
        

    def start_timer(self, time_limit):  
        while time_limit > 0:
            
            time_limit -= 1
            self.time_bar.setValue(time_limit)              
            self.time_counter.display((time_limit // 60) + 1)      
            time.sleep(1)

            if self.timer_paused:
                while self.timer_paused:
                    time.sleep(1)

            if not self.timer_running:
                break

        print('Done')
            

    def assign_fields(self, dict):
        self.title_label.setText(dict['title'])             # title
        self.scenario_text.setText(dict['scenario'])        # scenario

        # objectives
        self.line = QFrame(self.objectives_group)
        self.line.setFrameShape(QFrame.HLine)
        self.line.setFrameShadow(QFrame.Sunken)
        self.verticalLayout_3.addWidget(self.line)

        for objective in dict['objectives']:
            self.objective_label = QLabel(self.objectives_group)

            self.objective_label.setWordWrap(True)
            self.objective_label.setText(objective)

            self.line = QFrame(self.objectives_group)
            self.line.setFrameShape(QFrame.HLine)
            self.line.setFrameShadow(QFrame.Sunken)
            
            self.verticalLayout_3.addWidget(self.objective_label)
            self.verticalLayout_3.addWidget(self.line)

        # injects
        self.line2 = QFrame(self.injects_group)
        self.line2.setFrameShape(QFrame.HLine)
        self.line2.setFrameShadow(QFrame.Sunken)
        self.verticalLayout_5.addWidget(self.line2)        

        for inject in dict['injects']:
            self.horizontalLayout = QHBoxLayout()
            self.inject_label = QLabel(self.injects_group)
            sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
            sizePolicy.setHorizontalStretch(0)
            sizePolicy.setVerticalStretch(0)
            sizePolicy.setHeightForWidth(self.inject_label.sizePolicy().hasHeightForWidth())
            self.inject_label.setSizePolicy(sizePolicy)
            self.inject_label.setText(inject)
            self.inject_label.setWordWrap(True)
            self.send_inject_button = QToolButton(self.injects_group)
            self.send_inject_button.setText('Send')
            self.horizontalLayout.addWidget(self.inject_label)
            self.horizontalLayout.addWidget(self.send_inject_button)
            self.verticalLayout_5.addLayout(self.horizontalLayout)
            self.line = QFrame(self.injects_group)
            self.line.setFrameShape(QFrame.HLine)
            self.line.setFrameShadow(QFrame.Sunken)
            self.verticalLayout_5.addWidget(self.line) 

        # questions
        self.line3 = QFrame(self.questions_group)
        self.line3.setFrameShape(QFrame.HLine)
        self.line3.setFrameShadow(QFrame.Sunken)
        self.verticalLayout_6.addWidget(self.line3)

        for qaw in dict['qaw']:
            self.horizontalLayout = QHBoxLayout()
            self.question_label = QLabel(self.questions_group)
            sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
            sizePolicy.setHorizontalStretch(0)
            sizePolicy.setVerticalStretch(0)
            sizePolicy.setHeightForWidth(self.question_label.sizePolicy().hasHeightForWidth())
            self.question_label.setSizePolicy(sizePolicy)
            self.question_label.setText(qaw[0])
            self.question_label.setWordWrap(True)
            self.send_question_button = QToolButton(self.questions_group)
            self.send_question_button.setText('Send')
            self.horizontalLayout.addWidget(self.question_label)
            self.horizontalLayout.addWidget(self.send_question_button)
            self.verticalLayout_6.addLayout(self.horizontalLayout)
            self.line = QFrame(self.questions_group)
            self.line.setFrameShape(QFrame.HLine)
            self.line.setFrameShadow(QFrame.Sunken)
            self.verticalLayout_6.addWidget(self.line) 
                