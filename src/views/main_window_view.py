from PySide6.QtWidgets import QMainWindow, QMessageBox
from src.uic.main_window import Ui_MainWindow
from src.views.create_scenario_view import CreateScenario
from lite import Database


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setupUi(self)
        self.assign_widgets()
        self.show()


    def assign_widgets(self):
        self.create_scenario_button.clicked.connect(lambda: self.create_scenario())


    # Handles the creation of a new scenario
    def create_scenario(self):
        #region
        self.scenario = CreateScenario()              # create scenario object
        self.main_stack.addWidget(self.scenario)      # add object to main stack
        self.main_stack.setCurrentIndex(1)            # switch main stack to show created object

        # assign widgets
        self.scenario.back_button.clicked.connect(lambda: clear_and_back())                     # back button
        self.scenario.create_scenario_tab.currentChanged.connect(lambda: on_tab_change())       # create scenario tabbed widget


        # Handles the tab change in the create scenario page
        # On last tab, change next button to save button
        def on_tab_change():
            tab = self.scenario.create_scenario_tab
            next = self.scenario.next_button
            if tab.currentWidget().objectName() == 'tab_3':         # last tab
                next.setText("Save")
                next.clicked.disconnect()
                next.clicked.connect(lambda: save_and_back())       # next button becomes save button to save entries in database
            else:
                next.setText("Next")
                next.clicked.disconnect()
                next.clicked.connect(lambda: tab.setCurrentIndex(tab.currentIndex() + 1))   # next button changes tab to the next one


        # Change the main stack to the first one and delete the create scenario object
        def clear_and_back():
            self.main_stack.setCurrentIndex(0) 
            self.scenario.deleteLater()         # delete create scenario object


        # Save entries of the create scenario in the database
        def save_and_back():
            db = Database('scenes.db')              # create Database object
            db.create_db()                          # create tables if they do not exist

            data = self.scenario.get_values()       # get values from text fields
            data[0] = data[0].lower()               # lower case title to check for uniqueness

            get_title = "SELECT title FROM scenarios WHERE title = ?"
            title = db.query_db(get_title, [data[0]]) 

            empty = False           # this variable is true if any text field is empty
            for i in range(2,6):
                for item in data[i]:
                    if item == "":
                        empty = True        

            # if there are empty fields
            if data[0] == "" or data[1] == "" or empty:
                QMessageBox.warning(self.scenario, "Warning", "All fields must be filled !", QMessageBox.Ok)
            # if question and answer fields are not equal
            elif len(data[4]) != len(data[5]):
                QMessageBox.warning(self.scenario, "Warning", "All questions must be associated with an answer !", QMessageBox.Ok)
            # if title already exists in the database
            elif title:
                QMessageBox.warning(self.scenario, "Warning", "Title already exists !", QMessageBox.Ok)
            # constraints done -> save in database
            else:
                # Insert title / scenario
                insert_scenario = "INSERT INTO scenarios (title, scenario) VALUES (?, ?)"
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

                clear_and_back()    # change main stack to first page and delete create scenario object
        #endregion