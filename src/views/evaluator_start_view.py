from PySide6.QtWidgets import QWidget, QLabel, QFrame
from src.uic.evaluator_start import Ui_EvaluatorStart


class EvaluatorStart(QWidget, Ui_EvaluatorStart):
    def __init__(self):
        super(EvaluatorStart, self).__init__()
        self.setupUi(self)
        self.init_widgets()
        self.assign_widgets()
        
    
    def init_widgets(self):
        pass
    
    
    def assign_widgets(self):
        pass


    def assign_fields(self, dict):
        self.title_label.setText(dict['title'])
        self.scenario_text.setText(dict['scenario'])

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
        
        
