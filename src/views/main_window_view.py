from PySide6.QtWidgets import QMainWindow, QMessageBox
from src.uic.main_window import Ui_MainWindow
from src.views.create_scenario_view import CreateScenario
import lite


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setupUi(self)
        self.assign_widgets()
        self.show()


    def assign_widgets(self):
        self.create_scenario_button.clicked.connect(lambda: self.create_scenario())


    def create_scenario(self):
        self.scenario = CreateScenario()
        self.main_stack.addWidget(self.scenario)
        self.main_stack.setCurrentIndex(1)
        self.scenario.back_button.clicked.connect(lambda: clear_and_back())
        self.scenario.create_scenario_tab.currentChanged.connect(lambda: on_tab_change())


        def on_tab_change():
            tab = self.scenario.create_scenario_tab
            next = self.scenario.next_button
            if tab.currentWidget().objectName() == 'tab_3':
                next.setText("Save")
                next.clicked.disconnect()
                next.clicked.connect(lambda: save_and_back())
            else:
                next.setText("Next")
                next.clicked.disconnect()
                next.clicked.connect(lambda: tab.setCurrentIndex(tab.currentIndex() + 1))


        def save_and_back():
            #region
            data = self.scenario.get_values()
            empty = False
            for item in data[2]:
                if item == "":
                    empty = True
            for item in data[3]:
                if item == "":
                    empty = True
            for item in data[4]:
                if item == "":
                    empty = True
            for item in data[5]:
                if item == "":
                    empty = True

            if data[0] == "" or data[1] == "" or empty:
                QMessageBox.warning(self.scenario, "Warning", "All fields must be filled !", QMessageBox.Ok)
            else:
                save_to_db(data)
            #endregion
                

        def clear_and_back():
            self.main_stack.setCurrentIndex(0) 
            self.scenario.deleteLater()


        def save_to_db(data):
            #region
            cnx = lite.create_connection('scenes.db')
            data[0] = data[0].lower()

            # Create scenario table
            create_scenarios_table = """ 
            CREATE TABLE IF NOT EXISTS scenarios 
            (id INTEGER PRIMARY KEY AUTOINCREMENT, title TEXT UNIQUE, scenario TEXT,
            o1 TEXT, o2 TEXT, o3 TEXT, o4 TEXT, o5 TEXT,
            i1 TEXT, i2 TEXT, i3 TEXT, i4 TEXT, i5 TEXT)
            """
            lite.execute_query(cnx, create_scenarios_table)

            # Create questions / answers / weights table
            create_qaw_table = """
            CREATE TABLE IF NOT EXISTS qaw (scenario INTEGER, question TEXT, answer TEXT, weight INTEGER,
            FOREIGN KEY (scenario) REFERENCES scenarios(id))
            """
            lite.execute_query(cnx, create_qaw_table)

            # Check if title exists
            get_title = """ SELECT title FROM scenarios WHERE title = ? """
            title = lite.fetch_query_var(cnx, get_title, [data[0]])
            
            if title:
                QMessageBox.warning(self.scenario, "Warning", "Title already easists !", QMessageBox.Ok)
            elif len(data[4]) != len(data[5]):
                QMessageBox.warning(self.scenario, "Warning", "All questions must be associated with an answer !", QMessageBox.Ok)
            else:
                # Insert title / scenario
                insert_scenario = """ INSERT INTO scenarios (title, scenario) VALUES (?, ?) """
                lite.execute_query_var(cnx, insert_scenario, [data[0], data[1]])

                # Get scenario id
                get_scenario_id = """ SELECT id FROM scenarios WHERE title = ? """
                id = lite.fetch_query_var(cnx, get_scenario_id, [data[0]])[0][0]

                # Insert objectives
                for i in range(0, len(data[2])):
                    q = " UPDATE scenarios SET o" + str(i+1) + " = ? WHERE id = ? "
                    lite.execute_query_var(cnx, q, [data[2][i], id])

                # Insert injects
                for i in range(0, len(data[3])):
                    q = " UPDATE scenarios SET i" + str(i+1) + " = ? WHERE id = ? "
                    lite.execute_query_var(cnx, q, [data[3][i], id])

                # Insert questions / answers / weights
                for i in range(len(data[4])):
                    q = """ INSERT INTO qaw VALUES (?, ?, ?, ?) """
                    lite.execute_query_var(cnx, q, [id, data[4][i], data[5][i], data[6][i]])
                
                cnx.close()
                clear_and_back()
            #endregion    
