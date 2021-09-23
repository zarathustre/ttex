from PySide6.QtWidgets import QWidget, QTextEdit, QHBoxLayout, QComboBox
from src.uic.create_scenario_page import Ui_create_scenario_page


class CreateScenario(QWidget, Ui_create_scenario_page):
    def __init__(self):
        super(CreateScenario, self).__init__()
        self.setupUi(self)
        self.init_widgets()
        self.assign_widgets()


    def init_widgets(self):
        self.create_scenario_tab.setCurrentIndex(0)
        self.question_combo_box.setFixedWidth(50)
        for i in range(10):
            self.question_combo_box.addItem(str(i+1))


    def assign_widgets(self):
        self.next_button.clicked.connect(lambda: self.create_scenario_tab.setCurrentIndex(self.create_scenario_tab.currentIndex() + 1))
        self.add_objective_button.clicked.connect(lambda: self.add_objective())
        self.remove_objetive_button.clicked.connect(lambda: self.remove_objective())
        self.add_inject_button.clicked.connect(lambda: self.add_inject())
        self.remove_inject_button.clicked.connect(lambda: self.remove_inject())
        self.add_question_button.clicked.connect(lambda: self.add_question())
        self.remove_question_button.clicked.connect(lambda: self.remove_question())
        self.add_answer_button.clicked.connect(lambda: self.add_answer())
        self.remove_answer_button.clicked.connect(lambda: self.remove_answer())
        self.clear_button.clicked.connect(lambda: self.clear_text())


    def clear_text(self):
        tab = self.create_scenario_tab.currentWidget()
        if tab.objectName() == 'tab_1':
            self.title_edit.clear()
        if tab.objectName() == 'tab_3':
            combo_children = tab.findChildren(QComboBox)
            for child in combo_children:
                child.setCurrentIndex(0)
        children = tab.findChildren(QTextEdit)
        for child in children:
            child.clear()
        

    def add_objective(self):
        count = len(self.objectives_group.findChildren(QTextEdit))
        if count < 5:
            self.objectives_edit = QTextEdit(self.objectives_group)
            self.objectives_edit.setObjectName(f"objectives_edit_{count}")
            self.verticalLayout_3.addWidget(self.objectives_edit)
            self.objectives_edit.setTabChangesFocus(True)
            self.objectives_edit.setFocus()
            self.setTabOrder(self.objectives_group.findChildren(QTextEdit)[-2], self.objectives_group.findChildren(QTextEdit)[-1])

    def remove_objective(self):
        children = self.objectives_group.findChildren(QTextEdit)
        if len(children) > 1:  
            children[-1].deleteLater()
            children[-2].setFocus()


    def add_inject(self):
        count = len(self.injects_group.findChildren(QTextEdit))
        if count < 5:
            self.injects_edit = QTextEdit(self.injects_group)
            self.injects_edit.setObjectName(f"injects_edit_{count}")
            self.verticalLayout_4.addWidget(self.injects_edit)
            self.injects_edit.setTabChangesFocus(True)
            self.injects_edit.setFocus()
            self.setTabOrder(self.injects_group.findChildren(QTextEdit)[-2], self.injects_group.findChildren(QTextEdit)[-1])

    def remove_inject(self):
        children = self.injects_group.findChildren(QTextEdit)
        if len(children) > 1:  
            children[-1].deleteLater()
            children[-2].setFocus()


    def add_question(self):
        count = len(self.questions_group.findChildren(QTextEdit))
        if count < 5:
            self.question_edit = QTextEdit(self.questions_group)
            self.question_edit.setObjectName(f"question_edit_{count}")
            self.horizontalLayout = QHBoxLayout()
            self.horizontalLayout.addWidget(self.question_edit)
            self.question_combo_box = QComboBox(self.questions_group)
            self.question_combo_box.setObjectName(f"question_combo_box_{count}")
            self.question_combo_box.setFixedWidth(50)
            self.horizontalLayout.addWidget(self.question_combo_box)
            self.verticalLayout_6.addLayout(self.horizontalLayout)
            self.question_edit.setTabChangesFocus(True)
            self.question_edit.setFocus()
            self.setTabOrder(self.questions_group.findChildren(QTextEdit)[-2], self.questions_group.findChildren(QTextEdit)[-1])
            for i in range(10):
                self.question_combo_box.addItem(str(i+1))
            
    def remove_question(self):
        text_children = self.questions_group.findChildren(QTextEdit)
        combo_children = self.questions_group.findChildren(QComboBox)
        if len(text_children) > 1:  
            text_children[-1].deleteLater()
            combo_children[-1].deleteLater()
            text_children[-2].setFocus()


    def add_answer(self):
        count = len(self.answers_group.findChildren(QTextEdit))
        if count < 5:
            self.answer_edit = QTextEdit(self.answers_group)
            self.answer_edit.setObjectName(f"answer_edit_{count}")
            self.verticalLayout_7.addWidget(self.answer_edit)
            self.answer_edit.setTabChangesFocus(True)
            self.answer_edit.setFocus()
            self.setTabOrder(self.answers_group.findChildren(QTextEdit)[-2], self.answers_group.findChildren(QTextEdit)[-1])

    def remove_answer(self):
        children = self.answers_group.findChildren(QTextEdit)
        if len(children) > 1:  
            children[-1].deleteLater()
            children[-2].setFocus()


    def get_values(self):
        title = self.title_edit.text()
        scenario = self.scenario_edit.toPlainText()

        # Objectives
        objectives = []
        for obj in self.objectives_group.findChildren(QTextEdit):
            objectives.append(obj.toPlainText())

        # Injects
        injects = []
        for inj in self.injects_group.findChildren(QTextEdit):
            injects.append(inj.toPlainText())

        # Questions
        questions = []
        for ques in self.questions_group.findChildren(QTextEdit):
            questions.append(ques.toPlainText())

        # Weights
        weights = []
        for weight in self.questions_group.findChildren(QComboBox):
            weights.append(int(weight.currentText()))

        # Answers
        answers = []
        for answ  in self.answers_group.findChildren(QTextEdit):
            answers.append(answ.toPlainText())

        return [title, scenario, objectives, injects, questions, answers, weights]
