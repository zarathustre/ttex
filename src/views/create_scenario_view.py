from PySide6.QtWidgets import QWidget, QTextEdit, QHBoxLayout, QComboBox, QMessageBox

from src.uic.create_scenario_page import Ui_create_scenario_page
from src.lite import Database


class CreateScenario(QWidget, Ui_create_scenario_page):
    def __init__(self):
        super(CreateScenario, self).__init__()
        self.setupUi(self)
        self.init_widgets()
        self.assign_widgets()

    # Initialize widgets
    def init_widgets(self):
        self.create_scenario_tab.setCurrentIndex(0)
        self.question_combo_box.setFixedWidth(50)
        for i in range(10):
            self.question_combo_box.addItem(str(i+1))   # Add integers 1 to 10 to the weight combobox

    # Assign widgets (some are assigned in the main window view)
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

    # Handles the tab change in the create scenario page - On last tab, change next button to save button
    def on_tab_change(self, save_and_back):
        tab = self.create_scenario_tab
        next = self.next_button
        if tab.currentWidget().objectName() == 'tab_3':         # last tab
            next.setText("Save")
            self.next_button.setStatusTip('Save scenario in the database')
            next.clicked.disconnect()
            next.clicked.connect(lambda: save_and_back())       # next button becomes save button to save entries in database
        else:
            next.setText("Next")
            self.next_button.setStatusTip('Go to next tab')
            next.clicked.disconnect()
            next.clicked.connect(lambda: tab.setCurrentIndex(tab.currentIndex() + 1))   # next button changes tab to the next one

    # Clear the input fields of the current tab
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
        
    # Add an input for the objective field
    def add_objective(self):
        count = len(self.objectives_group.findChildren(QTextEdit))
        if count < 5:
            self.objectives_edit = QTextEdit(self.objectives_group)
            self.objectives_edit.setObjectName(f"objectives_edit_{count}")
            self.verticalLayout_3.addWidget(self.objectives_edit)
            self.objectives_edit.setTabChangesFocus(True)
            self.objectives_edit.setFocus()
            self.setTabOrder(self.objectives_group.findChildren(QTextEdit)[-2], self.objectives_group.findChildren(QTextEdit)[-1])

    # Remove added input for the objective field
    def remove_objective(self):
        children = self.objectives_group.findChildren(QTextEdit)
        if len(children) > 1:  
            children[-1].deleteLater()
            children[-2].setFocus()

    # Add an input for the inject field
    def add_inject(self):
        count = len(self.injects_group.findChildren(QTextEdit))
        if count < 5:
            self.injects_edit = QTextEdit(self.injects_group)
            self.injects_edit.setObjectName(f"injects_edit_{count}")
            self.verticalLayout_4.addWidget(self.injects_edit)
            self.injects_edit.setTabChangesFocus(True)
            self.injects_edit.setFocus()
            self.setTabOrder(self.injects_group.findChildren(QTextEdit)[-2], self.injects_group.findChildren(QTextEdit)[-1])

    # Remove added input for the inject field
    def remove_inject(self):
        children = self.injects_group.findChildren(QTextEdit)
        if len(children) > 1:  
            children[-1].deleteLater()
            children[-2].setFocus()

    # Add an input question field and a weight combobox
    def add_question(self):
        count = len(self.questions_group.findChildren(QTextEdit))
        if count < 5:
            self.question_edit = QTextEdit(self.questions_group)                    # question text edit
            self.question_edit.setObjectName(f"question_edit_{count}")              # set object name
            self.horizontalLayout = QHBoxLayout()                                   # layout
            self.horizontalLayout.addWidget(self.question_edit)                     # add wiget to layout
            self.question_combo_box = QComboBox(self.questions_group)               # weight combobox
            self.question_combo_box.setObjectName(f"question_combo_box_{count}")    # set object name
            self.question_combo_box.setFixedWidth(50)                               # fixed width
            self.horizontalLayout.addWidget(self.question_combo_box)                # add wiget
            self.verticalLayout_6.addLayout(self.horizontalLayout)                  # add wiget to layout        
            self.question_edit.setTabChangesFocus(True)
            self.question_edit.setFocus()
            # set tab button to change focus between fields
            self.setTabOrder(self.questions_group.findChildren(QTextEdit)[-2], self.questions_group.findChildren(QTextEdit)[-1])
            # add integers 1 to 10 to the weight combobox
            for i in range(10):
                self.question_combo_box.addItem(str(i+1))

    # Remove an added input for the question / weight fields     
    def remove_question(self):
        text_children = self.questions_group.findChildren(QTextEdit)
        combo_children = self.questions_group.findChildren(QComboBox)
        if len(text_children) > 1:  
            text_children[-1].deleteLater()
            combo_children[-1].deleteLater()
            text_children[-2].setFocus()

    # Add an input for the answer field
    def add_answer(self):
        count = len(self.answers_group.findChildren(QTextEdit))
        if count < 5:
            self.answer_edit = QTextEdit(self.answers_group)
            self.answer_edit.setObjectName(f"answer_edit_{count}")
            self.verticalLayout_7.addWidget(self.answer_edit)
            self.answer_edit.setTabChangesFocus(True)
            self.answer_edit.setFocus()
            self.setTabOrder(self.answers_group.findChildren(QTextEdit)[-2], self.answers_group.findChildren(QTextEdit)[-1])

    # Remove an added input for the answer field
    def remove_answer(self):
        children = self.answers_group.findChildren(QTextEdit)
        if len(children) > 1:  
            children[-1].deleteLater()
            children[-2].setFocus()

    # Returns the values in the input text fields
    def get_values(self):
        title = self.title_edit.text()
        scenario = self.scenario_edit.toPlainText()
        objectives = [obj.toPlainText() for obj in self.objectives_group.findChildren(QTextEdit)]
        injects = [inj.toPlainText() for inj in self.injects_group.findChildren(QTextEdit)]
        questions = [ques.toPlainText() for ques in self.questions_group.findChildren(QTextEdit)]
        weights = [int(weight.currentText()) for weight in self.questions_group.findChildren(QComboBox)]
        answers = [answ.toPlainText() for answ in self.answers_group.findChildren(QTextEdit)]

        return [title, scenario, objectives, injects, questions, answers, weights]

    # Check for all database saving constraints - Returns True if none are violated
    def check_constraints(self):
        db = Database('scenes.db')     # create Database object
        db.create_db()                 # create tables if they do not exist

        data = self.get_values()       # get values from text fields
        data[0] = data[0].lower()      # lower case title to check for uniqueness

        get_title = "SELECT title FROM scenarios WHERE title = ?"
        title = db.query_db(get_title, [data[0]]) 

        # condition True if there's any empty field
        for i in range(2,6):
            any_empty_field = any(item == "" for item in data[i])        

        # if there are empty fields
        if data[0] == "" or data[1] == "" or any_empty_field:
            QMessageBox.warning(self, "Warning", "All fields must be filled !", QMessageBox.Ok)
        # if question and answer fields are not equal
        elif len(data[4]) != len(data[5]):
            QMessageBox.warning(self, "Warning", "All questions must be associated with an answer !", QMessageBox.Ok)
        # if title already exists in the database
        elif title:
            QMessageBox.warning(self, "Warning", "Title already exists !", QMessageBox.Ok)
        # constraints done -> save in database
        else:
            return True

        return False

    # Saves the values in the input fields to the database
    def save_to_db(self):
        db = Database('scenes.db')     # create Database object

        data = self.get_values()       # get values from text fields
        data[0] = data[0].lower()      # lower case title to check for uniqueness

        # Insert title / scenario
        insert_scenario = "INSERT INTO scenarios (title, scenario, date) VALUES (?, ?, DATE('now', 'localtime'))"
        db.query_db(insert_scenario, [data[0], data[1]])

        # Get scenario id
        get_id = "SELECT id FROM scenarios WHERE title = ?"
        id = db.query_db(get_id, [data[0]])[0][0]

        # Insert objectives
        for i in range(len(data[2])):
            q = "UPDATE scenarios SET o" + str(i+1) + " = ? WHERE id = ?"
            db.query_db(q, [data[2][i], id])

        # Insert injects
        for i in range(len(data[3])):
            q = "UPDATE scenarios SET i" + str(i+1) + " = ? WHERE id = ?"
            db.query_db(q, [data[3][i], id])

        # Insert questions / answers / weights
        for i in range(len(data[4])):
            q = "INSERT INTO qaw VALUES (?, ?, ?, ?)"
            db.query_db(q, [id, data[4][i], data[5][i], data[6][i]])
